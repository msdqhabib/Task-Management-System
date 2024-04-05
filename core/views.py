from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Import Models
from tasks.models import Task
from tasks.forms import TaskForm


# Create your views here.


class HomeView(View):
    def get(self, request):

        try:
            task_query = Task.objects.all()
            total_tasks = task_query.count()
            pending_tasks = task_query.filter(status='incomplete').count()
            completed_tasks = task_query.filter(status='complete').count()
        except:
            total_tasks = 0
            pending_tasks = 0
            completed_tasks = 0

        context = {
            'total_tasks': total_tasks,
            'pending_tasks': pending_tasks,
            'completed_tasks': completed_tasks
        }
        return render(request, 'core/home.html', context)
