from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CreateUserForm, LoginForm, ThoughtForm


# Create your views here.
def homepage(request):
    
    return render(request, 'journal/index.html')


def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            messages.success(request, "User Created!")
            
            return redirect('login')
        
    context = {'RegistrationForm': form}
    
    return render(request, 'journal/register.html', context)


def login(request):
    
    form = LoginForm()
    
    if request.method == 'POST':
        
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')
                
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                
                auth.login(request, user)
                
                return redirect('dashboard')
    
    context = {'LoginForm': form}

    
    return render(request, 'journal/my_login.html', context)


def user_logout(request):
    
    auth.logout(request)
    
    return redirect("home")


@login_required(login_url='login')
def dashboard(request):
    
    return render(request, 'journal/dashboard.html')


@login_required(login_url='login')
def create_thought(request):
    
    form = ThoughtForm()
    
    if request.method == 'POST':
        
        form = ThoughtForm(request.POST)
        
        if form.is_valid():
            
            thought = form.save(commit=False)
            thought.user = request.user
            thought.save()
            
            return redirect('dashboard')
    
    context = {'CreateThoughtForm': form}
    
    return render(request, 'journal/create_thought.html', context)
