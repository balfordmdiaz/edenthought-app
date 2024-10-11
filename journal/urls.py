from django.urls import path
from django.contrib.auth import views as auth_views

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
    path('delete-thought/<str:pk>', views.delete_thought, name='delete-thought'),
    
    path('profile-management', views.profile_management, name='profile-management'),
    path('delete-account', views.delete_account, name='delete-account'),
    
    #password management
    path('reset-password', auth_views.PasswordResetView.as_view(template_name='journal/password_reset.html'), name='reset-password'),
    # show a success message than email was sent
    path('reset-password-sent', auth_views.PasswordResetDoneView.as_view(template_name='journal/password_reset_sent.html'), name='password_reset_done'),
    # send a link to our email, so that we can reset the password
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='journal/password_reset_form.html'), name='password_reset_confirm'),
    # Show a success message that our password was changed
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='journal/password_reset_complete.html'), name='password_reset_complete'),
]