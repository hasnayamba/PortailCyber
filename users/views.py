from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from django.db import IntegrityError
from .decorators import role_required


@role_required(['autorite', 'expert'])
def some_protected_view(request):
    # Ta logique ici
    return render(request, 'users/protected.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        role = request.POST.get('role')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Validation simple
        if not all([username, email, role, password, password2]):
            messages.error(request, "Veuillez remplir tous les champs.")
            return redirect('register')

        if password != password2:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return redirect('register')

        try:
            user = User.objects.create_user(username=username, email=email, role=role, password=password)
            user.save()
            messages.success(request, "Inscription réussie ! Vous pouvez maintenant vous connecter.")
            return redirect('login')
        except IntegrityError:
            messages.error(request, "Nom d’utilisateur ou email déjà utilisé.")
            return redirect('register')

    return render(request, 'users/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  
        else:
            messages.error(request, "Nom d’utilisateur ou mot de passe incorrect.")
            return redirect('login')

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Vous êtes déconnecté.")
    return redirect('login')


@login_required(login_url='login')
def dashboard_view(request):
    user = request.user
    return render(request, 'users/dashboard.html', {'user': user})

