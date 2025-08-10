from django.urls import path
from . import views

urlpatterns = [
    path('users/register/', views.register_view, name='register'),
    path('users/login/', views.login_view, name='login'),
    path('users/logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('protected/', views.some_protected_view, name='protected'),


]
