from django.urls import path
from .views import SignUpView, EagleLoginView, EagleLogoutView
from django.views.generic.base import TemplateView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", EagleLoginView.as_view(), name="login"),
    path("dashboard/", TemplateView.as_view(template_name="dashboard.html"), name="dashboard"),
    path("profile/", TemplateView.as_view(template_name="view_profile.html"), name="view_profile"),
    path('logout/', EagleLogoutView.as_view(), name='logout'),
]