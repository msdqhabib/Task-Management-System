from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.db.models import Q


# import models
from .models import Task
from .forms import TaskForm


class TaskView(View):
    def get(self, request):
        form = TaskForm()

        # Query filters
        title = request.GET.get('title', '')
        status = request.GET.get('status', '')
        sort_by = request.GET.get('sort_by', '')

        # Get tasks created by or assigned to the current user
        tasks = Task.objects.filter(
            Q(created_by=request.user) | Q(assigned_user=request.user)).order_by('task_priority')

        # Apply filters if they exist
        if title:
            tasks = tasks.filter(title__icontains=title)

        if status and status != 'all-tasks':
            tasks = tasks.filter(status=status)

        # Apply sorting if specified
        if sort_by == 'due_date':
            tasks = tasks.order_by('-due_date')
        elif sort_by == 'priority':
            tasks = sorted(
                tasks, key=lambda x: self.priority_value(x.task_priority))

        context = {
            'tasks': tasks,
            'form': form
        }
        return render(request, 'tasks/tasks.html', context)

    def post(self, request):
        form = TaskForm(request.POST)

        if form.is_valid():

            # Save the form data without committing to the database
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()

            messages.success(request, 'Task Saved Successfully')
            return redirect('task')

        else:
            messages.error(
                request, 'Task Creation Failed. Please Enter Valid Details')

            # Render the form with validation errors
            return render(request, 'tasks/tasks.html', {'form': form})

    def priority_value(self, priority):
        # Assign numeric values to each priority level
        priority_values = {
            'low': 3,
            'medium': 2,
            'high': 1
        }
        return priority_values.get(priority, 0)


class TaskDetailView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        task_id = self.kwargs['pk']

        # Check if the task exists
        task_instance = get_object_or_404(Task, id=task_id)

        # Check if the user has permission to access the task
        if task_instance.created_by == user or task_instance.assigned_user == user:
            form = TaskForm(instance=task_instance)

            context = {
                'form': form,
                'task': task_instance
            }

            return render(request, 'tasks/task_update.html', context)

        else:
            # Return 401 Unauthorized status if user does not have permission
            return HttpResponse(status=401)

    def post(self, request, *args, **kwargs):
        task_id = self.kwargs['pk']
        delete = request.POST.get('delete')

        # Check if the user wants to delete the task
        if not delete:
            task_instance = get_object_or_404(Task, id=task_id)

            form = TaskForm(request.POST, instance=task_instance)

            if form.is_valid():
                # Save the form data if valid and display success message
                form.save()
                messages.success(request, "Task Updated Successfully")

        else:
            # Delete the task and display success message
            task_instance = get_object_or_404(
                Task, id=task_id)
            task_instance.delete()
            messages.info(request, "Task Deleted Successfully")
        return redirect('home')
