from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as django_login
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken

@csrf_exempt
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        photo = request.FILES.get('photo')

        user = CustomUser.objects.create_user(username=email, email=email, password=password, first_name=name, last_name=surname)
        user.image = photo
        user.save()

        send_mail(
            'Bienvenue !',
            'Merci de vous être inscrit.',
            'abdelbenlaziz@gmail.com',
            [email],
            fail_silently=False,
        )

        return JsonResponse({'message': 'Inscription réussie.'})

    return JsonResponse({'error': 'Requête non valide.'})



    
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        django_login(request._request, user)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        return JsonResponse({
            'status': 'success', 
            'message': 'user bien login', 
            'access_token': access_token, 
            'refresh_token': str(refresh),
            'role': user.role_id,  
        })
    else:
        return JsonResponse({'status': 'error', 'message': 'user non login'})
    

def getUser(request):
    try:
        auth = JWTAuthentication()
        user, _ = auth.authenticate(request)
    except:
        return JsonResponse({'error': 'il y a une erreur'})
    mon_user = {
        'id': user.id,
        'username': user.username,
        'email': user.email
    }
    return JsonResponse({'user': mon_user})

@api_view(['POST'])
def logout(request):
    logout(request)
    return JsonResponse({'message': 'Déconnexion réussie.'})