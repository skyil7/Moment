from django.shortcuts import render, redirect
from board.models import Post

def home(request):
    if request.user.is_authenticated:#로그인 됨
        return mainList(request)
    else:#로그인 안됨
        return render(request, 'service.html')

def signup(request):
    return render(request, 'signup.html')

def mainList(request):
    object_list = Post.objects.all()
    print(object_list[0])
    return render(request, 'mainpage.html', {'object_list':object_list})