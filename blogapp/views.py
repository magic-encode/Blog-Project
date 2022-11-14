from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def blog_(request):
    return render(request, 'blog_.html')

def contact(request):
    return render(request, 'contact.html')


def profile(request):
    return render(request, 'login.html')


def lost_password(request):
    return render(request, 'lost-password.html')