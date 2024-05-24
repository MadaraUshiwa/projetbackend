from django.contrib import admin
from django.urls import path, include
from home.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path ('home/', home),
    path ('deleteBanner/<int:id>/', deleteBanner),
    path ('addBanner/', addBanner),
    path ('updateBanner/<int:id>/', updateBanner),
    path ('lireBanner/<int:id>/', lireBanner),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)