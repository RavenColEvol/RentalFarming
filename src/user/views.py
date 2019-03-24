from django.contrib.auth import logout
from django.shortcuts import render


def login_view(request):
    return render(request, 'user/login.html', {})


def logout_view(request):
    logout(request)
    return render(request, 'user/login.html', {})
