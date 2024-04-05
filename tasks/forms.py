from .models import Task
from django import forms
from django.forms import DateInput
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    assigned_user = forms.ModelChoiceField(
        queryset=User.objects.all(), empty_label="Please select", required=False, widget=forms.Select(attrs={'class': 'form-select', 'required': True}))

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date',
                  'assigned_user', 'status', 'task_priority']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title', 'required': True}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task description'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'task_priority': forms.Select(attrs={'class': 'form-select'}),
            'due_date': DateInput(attrs={'type': 'date', 'class': 'form-control', 'required': True}),

        }
