from django.contrib import admin
from django.urls import path, include
from services.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('services/', index_services),
    path('updateService/<int:id>/', updateService),
    path('readService/<int:id>/', readService),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
