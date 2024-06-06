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

def manager(request):
    managers = ManagerSerializer(Manager.objects.first(), many=False)
    return JsonResponse({"managers" : managers.data})
@api_view(['PUT'])
def updateManager(request):
    manager = Manager.objects.get(id=1)
    managers = ManagerSerializer(manager, data=request.data)
    if managers.is_valid():
        managers.save()
        return Response ({'success':'Élément modifié'})
    return Response({'error':'Erreur, élément non modifié'})  