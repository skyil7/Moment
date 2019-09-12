from django.urls import path, include
from django.conf.urls import url, include
from . import views
from .views import SignUpAPI, LoginAPI, UserAPI

urlpatterns = [
    url("^auth/signup/$", SignUpAPI.as_view()),
    url("^auth/login/$", LoginAPI.as_view()),
    url("^auth/user/$", UserAPI.as_view()),
]