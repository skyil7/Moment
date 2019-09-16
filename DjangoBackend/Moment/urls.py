from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('', include('account.urls')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
