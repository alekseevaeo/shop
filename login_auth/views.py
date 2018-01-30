from django.shortcuts import render, redirect
from django.contrib import auth
from login_auth.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


def register(request):
    username = auth.get_user(request).username
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegistrationForm()

        args = {'form': form}
    return render(request, 'login_auth/register.html', locals())


def view_profile(request):
    username = auth.get_user(request).username
    args = {
        'user': request.user
    }

    return render(request, 'login_auth/view_profile.html', locals())


def edit_profile(request):
    username = auth.get_user(request).username
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
        return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
    return render(request, 'login_auth/edit_profile.html', locals())