from django.contrib import admin
from django.urls import path, include
from services.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('services/', index_services),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
