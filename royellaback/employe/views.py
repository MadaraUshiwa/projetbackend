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

def employe(request):
    employees = employeSerializer(Employe.objects.all(), many=True)
    return JsonResponse({"employes":employees.data})

@api_view(['DELETE'])
def deleteEmployees(request, id):
    employee = Employe.objects.get(id=id)
    employee.delete()
    return Response({"message": "Employee was deleted successfully!"})

@api_view(['PUT'])
def updateEmployees(request, id):
    employee = Employe.objects.get(id=id)
    employees = employeSerializer(employee, data=request.data)
    if employees.is_valid():
        employees.save()
        return Response ({'success':'Élément modifié'})
    return Response({'error':'Erreur, élément non modifié'})  

def readEmployees(request, id):
    employee = employeSerializer(Employe.objects.get(id=id))
    return JsonResponse({'employee':employee.data})

@api_view(['POST'])
def createEmployees(request):
    employees = employeSerializer(data=request.data)
    if employees.is_valid():
        employees.save()
        return Response(employees.data)
    return Response(employees.errors)
