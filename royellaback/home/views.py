from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
import json

# Create your views here.
def home(request):
    banners = BannerSerializer(Banner.objects.all(), many=True)
    return JsonResponse({"banner" : banners.data})

@api_view(["DELETE"])
def deleteBanner(request, id):
    banner = Banner.objects.get(id=id)
    banner.delete()
    return Response("Effacé avec succés")

@api_view(["POST"])
def addBanner(request):
    banner = BannerSerializer(data=request.data)
    if banner.is_valid():
        banner.save()
        return Response(banner.data)
    return Response(banner.errors)

@api_view(["PUT"])
def updateBanner(request, id):
    banner = Banner.objects.get(id=id)
    banners = BannerSerializer(banner, data=request.data)
    if banners.is_valid():
        banners.save()
        return Response("Modifié avec succés")
    return Response(banners.errors)

def lireBanner(request, id):
    banner = Banner.objects.get(id=id)
    banners = BannerSerializer(banner)
    return JsonResponse({"banner" : banners.data})
