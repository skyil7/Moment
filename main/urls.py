from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='mainpage'),
    path('/signup', views.signup, name='signup'),
]