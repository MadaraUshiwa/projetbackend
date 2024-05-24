from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Manager(models.Model):
    nom = models.CharField(max_length=70)
    poste = models.CharField(max_length=70)
    image = models.ImageField(upload_to='images/')
    citation = models.TextField()
