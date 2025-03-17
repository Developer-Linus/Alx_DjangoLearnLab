from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    
    # Custom views for registration and profile
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile, name='profile'),
]