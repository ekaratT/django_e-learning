from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'courses/index.html')


def login_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        print('user is logged in...')
        return redirect(reverse('index'))
    return render(request, 'courses/login.html')


def logout_page(request):
    logout(request)
    return render(request, 'courses/logged_out.html')

