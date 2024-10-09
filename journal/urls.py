from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'), 
    path('logout', views.user_logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('create-thought', views.create_thought, name='create-thought'),
    path('my-thoughts', views.my_thoughts, name='my-thoughts'),
    path('update-thought/<str:pk>', views.update_thought, name='update-thought'),
]