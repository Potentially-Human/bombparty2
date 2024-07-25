from django.urls import path

from . import views

from login.views import ChangePasswordView

urlpatterns = [
    path("login", views.loginview, name="login"),
    path("createaccount", views.createUser, name="createaccount"),
    path("logout", views.logoutview, name="logout"),
    path("profile/edit", views.editProfile, name="edit_profile"),
    path("profile", views.profile, name="profile"),
    path("profile/<str:username>", views.viewProfile, name="view_profile"),
    path("changepassword", ChangePasswordView.as_view(), name="changepassword"),
]