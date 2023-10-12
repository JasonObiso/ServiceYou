from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from .forms import LoginForm

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('success')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('success')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})