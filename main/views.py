from django.shortcuts import render, redirect
from board.models import Post, Category, Tag

def home(request):
    if request.user.is_authenticated:#로그인 됨
        return mainList(request)
    else:#로그인 안됨
        return render(request, 'service.html')

def signup(request):
    return render(request, 'signup.html')

def mainList(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'mainpage.html', {'posts':posts, 'categories':categories, 'tags':tags})