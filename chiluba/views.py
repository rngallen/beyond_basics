from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import datetime


@login_required
def index(request):
    context = {
        "date_today": datetime.datetime.now().date(),
    }
    return render(request, "main/index.html", context)


def login_view(request):
    form = AuthenticationForm(request.POST or None)
    context = {
        "form": form,
    }
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None and user.is_director == False:
            login(request, user)
            if request.GET.get("next"):
                return redirect(request.GET.get("next"))
        else:
            return render(request, "main/login.html", context)
    return render(request, "main/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("index")
