from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
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

        try:
            # Query filters
            task_search = request.GET.get('task_search', '')
            status = request.GET.get('status', '')

            sort_by = request.GET.get('sort_by', '')

            # Get tasks created by or assigned to the current user
            tasks = Task.objects.filter(
                Q(created_by=request.user) | Q(assigned_user=request.user)).order_by('task_priority')

            # Apply filters if they exist
            if task_search:
                tasks = tasks.filter(Q(title__icontains=task_search) |
                                     Q(description__icontains=task_search))
                context = {
                    'tasks': tasks,
                    'form': form
                }
                return render(request, 'tasks/tasks.html', context)

            elif status and status != 'all-tasks':
                # Apply status filters
                tasks = tasks.filter(status=status)

                # Render HTML template with tasks data
                tasks_html = render_to_string(
                    'tasks/tasks.html', {'tasks': tasks, 'form': form})

                return HttpResponse(tasks_html)

            elif sort_by:
                # Apply sorting if specified
                if sort_by == 'due_date':
                    tasks = tasks.order_by('-due_date')

                elif sort_by == 'priority':
                    tasks = sorted(
                        tasks, key=lambda x: self.priority_value(x.task_priority))
                # Render HTML template with tasks data
                tasks_html = render_to_string(
                    'tasks/tasks.html', {'tasks': tasks, 'form': form})

                return HttpResponse(tasks_html)

            context = {
                'tasks': tasks,
                'form': form
            }
            return render(request, 'tasks/tasks.html', context)
        except Exception as e:
            messages.error(
                request, f'Tasks Error - {e}')
            return render(request, 'tasks/tasks.html')

    def post(self, request):
        form = TaskForm(request.POST)
        try:
            if form.is_valid():

                # Save the form data without committing to the database
                task = form.save(commit=False)
                task.created_by = request.user
                # Assign the team ID from the form

                if 'team' in form.cleaned_data and form.cleaned_data['team']:
                    task.team = form.cleaned_data['team']

                task.save()

                messages.success(request, 'Task Saved Successfully')
                return redirect('task')

            else:
                messages.error(
                    request, 'Task Creation Failed. Please Enter Valid Details')

                # Render the form with validation errors
                return render(request, 'tasks/tasks.html', {'form': form})
        except Exception as e:
            messages.error(
                request, f'Task Creation Failed. Error - {e}')

            return render(request, 'tasks/tasks.html')

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
        try:
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
        except Exception as e:
            messages.error(
                request, f'Error in Task Detail - {e}')

            return render(request, 'tasks/tasks.html')

    def post(self, request, *args, **kwargs):
        try:
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

        except Exception as e:
            messages.error(
                request, f'Error in Task Updating - {e}')

            return render(request, 'tasks/tasks.html')
