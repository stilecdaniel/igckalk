from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("home/", login_required(views.home), name="home"),
    path("register/", views.register, name="register"),
    path("register/pending-auth/", views.auth, name="auth"),
    path("contacts/", views.contact, name="conts"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_info, name="profile_info"),
    path("password/", views.change_password, name="change_password"),
]

