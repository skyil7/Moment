from django.shortcuts import render
from .serializer import UserSerializer, SignUpSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from .permissions import IsAuthenticatedOrCreate

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)