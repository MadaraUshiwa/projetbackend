from django.contrib import admin
from django.urls import path, include
from employe.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path ('employe/', Employe),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
