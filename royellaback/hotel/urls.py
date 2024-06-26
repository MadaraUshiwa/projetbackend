from django.contrib import admin
from django.urls import path, include
from hotel.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path ('hotel/', Hotel),
    path('updateHotel/', updateHotel)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)