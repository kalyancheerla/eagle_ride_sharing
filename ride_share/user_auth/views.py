from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

class EagleLoginView(LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("dashboard")
    template_name = "login.html"

    def get_success_url(self):
        return self.success_url

class EagleLogoutView(LogoutView):
    success_url = reverse_lazy("home")

    def get_success_url(self):
        return self.success_url