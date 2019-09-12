from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from account import urls as accounturls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/', include(accounturls)),
    url(r'^api/auth', include('knox.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)