from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('post/write/', views.PostCreate.as_view(), name='create'),
    path('post/read/<int:pk>',views.PostRead.as_view(), name='read'),
    path('post/delete/<int:pk>', views.PostDelete.as_view(), name='delete'),
]