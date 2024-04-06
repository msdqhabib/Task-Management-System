from django.db import models
from teams.models import Team
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    created_on = models.DateField(auto_now=True, null=True, blank=True)
    assigned_user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_task', null=True, blank=True)
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=True, blank=True)

    STATUS_CHOICES = [
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete')
    ]
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='incomplete')

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]

    task_priority = models.CharField(
        max_length=20, choices=PRIORITY_CHOICES, default='low')

    def __str__(self):
        return self.title
