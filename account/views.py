from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signupProc(request):
    if request.method=="POST":
        if request.POST['password']==request.POST['confpass']:
            user = User.objects.create_user(
                username=request.POST['username'],password=request.POST['password']
            )
            auth.login(request, user)
            return redirect('mainpage')
    return render(request, 'signup.html', {'error':'SignUp Failed'})

def loginProc(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(request,username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('mainpage')
        else :
            return render(request, 'mainpage', {'error':'Username or Password is incorrect'})
    return redirect('mainpage')

def logout(request):
    auth.logout(request)
    return redirect('mainpage')