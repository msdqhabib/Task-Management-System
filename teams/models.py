from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_on = models.DateField(auto_now=True, null=True, blank=True)
    assigned_user = models.ManyToManyField(
        User, related_name='teams_assigned', null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_team', null=True, blank=True)

    def __str__(self):
        return self.title
