from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (PasswordChangeForm, SetPasswordForm)

from mooc.utils import generate_hash_key

from .forms import RegisterUserForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset

User = get_user_model()

@login_required
def dashboard(request):
    context = {

    }
    return render(request, "accounts/dashboard.html")

@login_required
def edit_password(request):
    context = {}
    if request.POST:
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context["success"] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context["form"] = form
    return render(request, "accounts/edit_password.html", context)

def reset_password(request):
    template_name = "accounts/reset_password.html"
    form = PasswordResetForm(request.POST or None)
    context = {}
    if form.is_valid():
        form.save()        
        context["sucesso"] = True

    context["form"] = form
    
    return render(request, template_name, context)

def confirm_reset_password(request, key):
    template_name = "accounts/confirm_reset_password.html"
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        context["sucesso"] = True

    context["form"] = form

    return render(request, template_name, context)

@login_required
def edit(request):
    context = {}
    if request.POST:
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context["success"] = True
    else:
        form = EditAccountForm(instance=request.user)
    context["form"] = form
    return render(request, "accounts/edit.html", context)

def register(request):
    if request.POST:
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                email=user.email, 
                password=form.cleaned_data["password1"]
            )
            login(request, user)
            return redirect("core:home")
    else :
        form = RegisterUserForm()
    context = {
        "form": form
    }
    return render(request, "accounts/register.html", context)
    

