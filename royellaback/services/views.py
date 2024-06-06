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

def index_services(request):
    services = ServicesSerializer(Services.objects.all(), many=True)
    return JsonResponse({"services" : services.data})

def readService(request, id):
    service = ServicesSerializer(Services.objects.get(id=id))
    return JsonResponse({'service':service.data})

@api_view(['PUT'])
def updateService(request, id):
    service = Services.objects.get(id=id)
    services = ServicesSerializer(service, data=request.data)
    if services.is_valid():
        services.save()
        return Response ({'success':'Élément modifié'})
    return Response(services.errors)        