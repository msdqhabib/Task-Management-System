from .models import Team
from django import forms
from django.forms import DateInput
from django.contrib.auth.models import User


class TeamForm(forms.ModelForm):
    assigned_user = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.SelectMultiple(
            attrs={'class': 'form-select', 'required': True}),
        required=False
    )

    class Meta:
        model = Team
        fields = ['title', 'description', 'assigned_user']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title', 'required': True}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Task description'}),

        }
