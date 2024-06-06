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

def Hotel(request):
    hotels = hotelSerializer(hotel.objects.get(id=1))
    return JsonResponse({"hotels" : hotels.data})

@api_view(['PUT'])
def updateHotel(request):
    hotel1 = hotel.objects.get(id=1)
    hotels = hotelSerializer(hotel1, data=request.data)
    if hotels.is_valid():
        hotels.save()
        return Response ({'success':'Élément modifié'})
    return Response(hotels.errors)           