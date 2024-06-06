from django.contrib import admin
from django.urls import path, include
from manager.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path ('manager/', manager),
    path('updateManager/', updateManager),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
