from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signupProc/',views.signupProc,name='signupProc'),
    path('loginProc/',views.loginProc,name='loginProc'),
    path('logout/',views.logout,name='logout'),
]