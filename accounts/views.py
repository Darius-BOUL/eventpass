from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('event_list')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Récupère automatiquement l'utilisateur validé
            login(request, user)
            next_url = request.GET.get('next') or 'event_list'
            return redirect(next_url)
        else:
            messages.error(request, 'Nom d’utilisateur ou mot de passe incorrect.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
