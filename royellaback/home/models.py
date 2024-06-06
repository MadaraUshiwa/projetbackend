from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Banner(models.Model):
    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    stars = models.IntegerField()