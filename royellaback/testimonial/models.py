from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Testimonial(models.Model):
    nom = models.CharField(max_length=100)
    note = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    testimon = models.TextField()
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
