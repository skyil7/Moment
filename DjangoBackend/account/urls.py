from django.conf.urls import url, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^signup/$', SignUp.as_view(), name="sign_up"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]