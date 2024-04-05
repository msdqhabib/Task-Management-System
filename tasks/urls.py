from django.urls import path
from .views import TaskView, TaskDetailView

urlpatterns = [
    path('task/', TaskView.as_view(), name='task'),
    path('task/<int:pk>/',
         TaskDetailView.as_view(), name='task-update'),
]
