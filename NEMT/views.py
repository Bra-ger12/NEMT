
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def base(request):
    messages.success(request, "login successfully")
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'service.html')

@login_required
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
          
            return redirect('base')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        return redirect('login')

    return render(request, 'reg.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('base.html')
