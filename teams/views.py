from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from tasks.models import Task
from .models import Team
from .forms import TeamForm
from tasks.forms import TaskForm
from django.db.models import Q
from django.contrib import messages


class TeamView(View):
    def get(self, request):

        form = TeamForm()

        # Query filters
        team_search = request.GET.get('team_search', '')
        team_title = request.GET.get('team', '')
        print(f'team_title - {team_title}')

        # Get team created by or assigned to the current user
        teams = Team.objects.filter(
            Q(created_by=request.user) | Q(assigned_user__username=request.user)).distinct()

        # Apply filters if they exist
        if team_search:
            teams = teams.filter(Q(title__icontains=team_search) |
                                 Q(description__icontains=team_search))

        context = {
            'teams': teams,
            'form': form,
        }

        if team_title:
            # Get the team object
            team_instance = Team.objects.get(title=team_title)
            # Get the users associated with the team
            users = team_instance.assigned_user.all()

            # Render the users as options for the assigned user field
            options = [{'value': user.pk, 'label': user.username}
                       for user in users]
            print(f'options - {options}')
            return JsonResponse({'options': options})

        return render(request, 'teams/teams.html', context)

    def post(self, request):
        form = TeamForm(request.POST)

        if form.is_valid():
            # Save the form data without committing to the database
            team = form.save(commit=False)
            team.created_by = request.user
            team.save()

            print(f"form.cleaned_data- {form.cleaned_data['assigned_user']}")
            assigned_users = form.cleaned_data['assigned_user']
            team.assigned_user.set(assigned_users)

            messages.success(request, 'Team Created Successfully')
            return redirect('team')

        else:
            messages.error(
                request, 'Team Creation Failed. Please Enter Valid Details')

            # Render the form with validation errors
            return render(request, 'teams/teams.html', {'form': form})

    def get_users_by_team(self, request):
        team_id = request.GET.get('team_id')
        if team_id:
            # Get the team object
            team = get_object_or_404(Team, id=team_id)
            # Get the users associated with the team
            users = team.assigned_user.all()
            # Render the users as options for the assigned user field
            options = ''.join(
                [f'<option value="{user.pk}">{user.username}</option>' for user in users])
            return JsonResponse({'options': options})
        else:
            return JsonResponse({'options': ''})


class TeamDetailView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        task_id = self.kwargs['pk']

        task_form = TaskForm()

        # Check if the task exists
        team_instance = get_object_or_404(Team, id=task_id)

        # Check if the user has permission to access the team
        if team_instance.created_by == user or team_instance.assigned_user.filter(pk=user.pk).exists():
            form = TeamForm(instance=team_instance)

            # get this team tasks
            team_tasks = Task.objects.filter(team__title=team_instance.title)

            context = {
                'form': form,
                'task_form': task_form,
                'team': team_instance,
                'team_tasks': team_tasks
            }

            return render(request, 'teams/team_update.html', context)

        else:
            # Return 401 Unauthorized status if user does not have permission
            return HttpResponse(status=401)

    def post(self, request, *args, **kwargs):
        task_id = self.kwargs['pk']
        delete = request.POST.get('delete')

        # Check if the user wants to delete the task
        if not delete:
            task_instance = get_object_or_404(Team, id=task_id)

            form = TeamForm(request.POST, instance=task_instance)

            if form.is_valid():
                # Save the form data if valid and display success message
                form.save()
                messages.success(request, "Team Updated Successfully")

        else:
            # Delete the task and display success message
            task_instance = get_object_or_404(
                Team, id=task_id)
            task_instance.delete()
            messages.info(request, "Team Deleted Successfully")
        return redirect('team')
