from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages


class RegisterView(View):
    template_name = 'authentication/register.html'
    form_class = UserCreationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Account created successfully. You can now log in.')
            return redirect('login')
        else:
            # If form data is invalid, display error messages
            messages.error(
                request, f'Failed to create account. Please enter correct details')
            return render(request, self.template_name, {'form': form})
