from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login
from .forms import RegisterUserForm

def register(request):
    if request.POST:
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, 
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

