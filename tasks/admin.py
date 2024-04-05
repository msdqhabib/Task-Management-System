from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'due_date',
                    'assigned_user', 'status', 'task_priority']


admin.site.register(Task, TaskAdmin)
