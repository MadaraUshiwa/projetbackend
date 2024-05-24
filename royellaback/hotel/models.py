from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class hotel(models.Model):
    titre = models.CharField(max_length=70)
    description = models.TextField()
    video = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/')
    localisation = models.CharField(max_length=100)
    
    
