from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='landingPage'),
    path('register/', views.register, name='register'),
    path('userlogin/', views.UserLogin, name='userlogin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard_menu/', views.dashboard_menu, name='dashboard_menu'),
    path('userlogout/', views.UserLogout, name='userlogout'),
    
    
]