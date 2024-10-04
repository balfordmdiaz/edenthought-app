from django.shortcuts import render

# Create your views here.
def homepage(request):
    
    return render(request, 'journal/index.html')

def register(request):
    
    return render(request, 'journal/register.html')


def login(request):
    
    return render(request, 'journal/my_login.html')


def dashboard(request):
    
    return render(request, 'journal/dashboard.html')
