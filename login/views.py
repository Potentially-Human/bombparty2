from django.shortcuts import render, redirect
# from django import forms
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse, reverse_lazy
# from django.contrib.auth import authenticate, login, logout
from . forms import UserCreation, LoginForm, UpdateProfileForm, UpdateUserForm

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout 

from . models import UserProfile

from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import PasswordChangeView

class ChangePasswordView(PasswordChangeView):
    template_name = "login/change_password.html"
    success_url = reverse_lazy("game")

# Create your views here.
def loginview(request):
    if request.user.username:
        return redirect("game")

    form = LoginForm()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("game"))
        else:
            return render(request, "login/login.html", {
                "loginform": form,
                "message": "Invalid User",
            })
    
    return render(request, "login/login.html", {
        "loginform": form
    })

def createUser(request):
    if request.user.username:
        return redirect("game")

    form = UserCreation()
    message = ""

    if request.method == "POST":
        form = UserCreation(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            nickname = form.cleaned_data.get("nickname")
            user = User.objects.get(username = username)
            user_profile = UserProfile.objects.create(user = user, nickname = nickname)
            user_profile.save()

            return redirect("login")
        message = "Please retry"

    errorList = form.errors.as_data()

    parsableErrorList = {}

    for field, error in errorList.items():
        if field == "password1" or field == "password2":
            try: 
                parsableErrorList[0].append(error[0].messages[0])
            except (KeyError):
                parsableErrorList[0] = []
                parsableErrorList[0].append(error[0].messages[0])
        else: 
            try: 
                parsableErrorList[field.capitalize()].append(error[0].messages[0])
            except (KeyError):
                parsableErrorList[field.capitalize()] = []
                parsableErrorList[field.capitalize()].append(error[0].messages[0])

    return render(request, "login/createaccount.html", {
        'createuserform': form,
        'message': message,
        'errordict': parsableErrorList,
    })

def logoutview(request):
    logout(request)
    return redirect('game')

@login_required
def editProfile(request):
    message = ""
    error = ""
    if request.method == "POST":
        update_user_form = UpdateUserForm(request.POST, instance = request.user)
        update_profile_form = UpdateProfileForm(request.POST, request.FILES, instance = request.user.userprofile)

        if update_user_form.is_valid() and update_profile_form.is_valid():
            update_user_form.save()
            update_profile_form.save()
            message = "Profile has been updated successfully"
            return redirect("profile")
        else:
            error = "Could Not Update Profile"
    else:
        update_user_form = UpdateUserForm(instance = request.user)
        update_profile_form = UpdateProfileForm(instance = request.user.userprofile)
    
    return render(request, "login/editprofile.html", {
        "update_user_form": update_user_form,
        "update_profile_form": update_profile_form,
        "message": message, 
    })

@login_required      
def profile(request):
    return redirect("view_profile", username = request.user.username)

def viewProfile(request, username):
    try:
        user = User.objects.get(username = username)
        return render(request, "login/profile.html", {
            "user": user, 
        })
    except:
        return render(request, "login/404.html")

