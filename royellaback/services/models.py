from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Services(models.Model):
    theme = models.CharField(max_length=70)
    titre = models.CharField(max_length=70)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField()
    ordre = models.IntegerField()
