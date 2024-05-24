# authentification/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'photo']