from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('Login')
    template_name = "registration/register.html"