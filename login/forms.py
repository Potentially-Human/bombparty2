from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import TextInput, PasswordInput

from django.core.validators import MaxValueValidator, MinValueValidator

from .models import UserProfile

class UserCreation(UserCreationForm):
    nickname = forms.CharField(max_length = 32, min_length = 1, required = True, widget = TextInput(attrs = {"class": "nicknameInput", "placeholder": "Nickname"}))

    class Meta:
        model = User
        fields = ["username", "nickname", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = TextInput(attrs = {
        "placeholder": "Username"
    }))
    password = forms.CharField(widget = PasswordInput(attrs = {
        "placeholder": "Password"
    }))

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(widget = forms.TextInput(), max_length = 100, required = True)

    class Meta:
        model = User
        fields = ['username']


class UpdateProfileForm(forms.ModelForm):
    nickname = forms.CharField(widget = forms.TextInput(), max_length = 32, required = True)
    profile_picture = forms.ImageField()

    class Meta:
        model = UserProfile
        fields = ["nickname", "profile_picture"]


