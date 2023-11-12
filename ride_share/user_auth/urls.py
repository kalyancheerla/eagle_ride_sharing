from django.urls import path

from .views import SignUpView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", SignUpView.as_view(), name="user_login"),
    path("signout/", SignUpView.as_view(), name="signout"),
]