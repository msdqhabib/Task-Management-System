from django import forms
from django.forms import DateInput
from django.contrib.auth.models import User

# import models
from .models import Task
from teams.models import Team


class TaskForm(forms.ModelForm):
    assigned_user = forms.ModelChoiceField(
        queryset=User.objects.all(), empty_label="Please select user", required=False, widget=forms.Select(attrs={'class': 'form-select', 'required': True}))
    team = forms.ModelChoiceField(
        queryset=Team.objects.all(), empty_label="Please select team", required=False, widget=forms.Select(attrs={'class': 'form-select', 'required': True}))

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'team',
                  'assigned_user', 'status', 'task_priority']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title', 'required': True}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task description'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'task_priority': forms.Select(attrs={'class': 'form-select'}),
            'due_date': DateInput(attrs={'type': 'date', 'class': 'form-control', 'required': True}),

        }
