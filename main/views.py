from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def signIn(request):
    if request.method == 'POST':
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
    pass

def signUp(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.info(request, 'Account successfully created for ' + str(username.upper()))
            return redirect('/sign-in')
        else:
            messages.info(request, 'Error! Correct form errors and try again.')
        
    return render(request, 'main/sign-up.html', {'form': form})