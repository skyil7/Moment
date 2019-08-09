from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        return render(request, 'mainpage.html')
    else:
        return render(request, 'service.html')

def signup(request):
    return render(request, 'signup.html')