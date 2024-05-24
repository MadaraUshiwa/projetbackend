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

def room(request):
    rooms = RoomSerializer(Room.objects.all(), many=True)
    amenities = AmenitySerializer(Amenity.objects.all(), many=True)
    return JsonResponse({"rooms" : rooms.data, "amenities" : amenities.data})
