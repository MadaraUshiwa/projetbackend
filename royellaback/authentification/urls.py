from django.urls import path
from .views import register
from .views import login
from .views import getUser
from .views import logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('getUser/', getUser, name='getUser'),
    path('logout/', logout, name='logout')
]