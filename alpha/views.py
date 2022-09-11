from ast import Pass
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .models import Service
from .forms import Registration

# Create your views here.

def landing(request):
    services = Service.objects.all()
    context = {'service': services}
    return render (request, 'alpha/landing.html', context)

@login_required(login_url='userlogin')
def dashboard(request):
    return render (request, 'alpha/dashboard.html')

def dashboard_menu(request):
    return render (request, 'alpha/dashboard_menu.html')

def UserLogin(request):
    if request.user.is_authenticated:
        return redirect('dashboard_menu')
    
    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard_menu') 
        else:
            messages.error(request, 'Username or password is incorrect')

    return render (request, 'alpha/login.html')

def register(request):
    form = Registration()
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
       
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            

            messages.success(request, 'Account was created successfully, login to proceed')

            return redirect('userlogin')
        else:
            messages.error(request, 'An error has occured during registration')
    context = {'form': form}
    return render(request, 'alpha/register.html', context)

def UserLogout(request):
    logout(request)
    messages.error(request, 'logged out successfully')
    return redirect('userlogin')
         

