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

def contact(request):
    contact = ContactSerializer(Contact.objects.get(id=1))
    return JsonResponse({"contact" : contact.data})

@api_view(['PUT'])
def updateContact(request):
    contact = Contact.objects.get(id=1)
    contacts = ContactSerializer(contact, data=request.data)
    if contacts.is_valid():
        contacts.save()
        return Response ({'success':'Élément modifié'})
    return Response(contact.errors)        
