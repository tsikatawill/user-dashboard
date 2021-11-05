from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *

# Create your views here.
def home(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'main/index.html')
    else:
        return redirect('sign-in')

def signIn(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
       
        if user is not None:
            login(request, user)
            messages.success(request, f"{request.POST.get('username')}, logged in successfully")
            return redirect('home')
        else:
            messages.info(request, 'Wrong username and/or password')

    return render(request, 'main/sign-in.html')

def signOut(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('sign-in')

def signUp(request):
    form = CreateUserForm()
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    elif request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.info(request, 'Account successfully created for ' + str(username.upper()))
            return redirect('/sign-in')
        else:
            messages.info(request, 'Error! Correct form errors and try again.')
        
    return render(request, 'main/sign-up.html', {'form': form})