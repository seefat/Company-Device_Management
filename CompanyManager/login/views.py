from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('management:home')
    else:
        form = UserCreationForm()
    return render(request, 'log/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('management:home')
    else:
        form = AuthenticationForm()
    return render(request, 'log/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('management:home')

def to_redirect(request):
    if request.user.is_authenticated:
        return redirect('management:home')  # replace 'home' with the name of your home page URL pattern
    else:
        return redirect('log:login')  # replace 'log:login' with the name of your login page URL pattern

