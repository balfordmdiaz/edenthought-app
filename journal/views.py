from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import CreateUserForm, LoginForm, ThoughtForm, UpdateUserForm

from .models import Thought


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
            
            return redirect('my-thoughts')
    
    context = {'CreateThoughtForm': form}
    
    return render(request, 'journal/create_thought.html', context)


@login_required(login_url='login')
def my_thoughts(request):
    
    current_user = request.user.id
    
    thought = Thought.objects.all().filter(user=current_user)
    
    context = {'AllThoughts': thought}

    return render(request, 'journal/my_thoughts.html', context)


@login_required(login_url='login')
def update_thought(request, pk):
    
    try:
        thought = Thought.objects.get(id=pk, user=request.user)
        
    except:
        return redirect('my-thoughts')
    
    form = ThoughtForm(instance=thought)
    
    if request.method == 'POST':
        
        form = ThoughtForm(request.POST, instance=thought)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('my-thoughts')
            
    context = {'UpdateThought': form}
    
    return render(request, 'journal/update_thought.html', context)


@login_required(login_url='login')
def delete_thought(request, pk):

    try:
        thought = Thought.objects.get(id=pk, user=request.user)
        
    except:
        return redirect('my-thoughts')
    
    
    if request.method == 'POST':
        
        thought.delete()
        
        return redirect('my-thoughts')

    return render(request, 'journal/delete_thought.html')


@login_required(login_url='login')
def profile_management(request):
    
    form = UpdateUserForm(instance=request.user)
    
    if request.method == 'POST':
        
        form = UpdateUserForm(request.POST, instance=request.user)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('dashboard')
        
    context = {'ProfileForm': form}

    return render(request, 'journal/profile_management.html', context)


@login_required(login_url='login')
def delete_account(request):
    
    if request.method == 'POST':
        
        deleteUser = User.objects.get(username=request.user)
        
        deleteUser.delete()
        
        return redirect('home')

    return render(request, 'journal/delete_account.html')