from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Amenity(models.Model):
    titre = models.CharField(max_length=70)
    image = models.CharField(max_length=100)

class Room(models.Model):
    titre = models.CharField(max_length=70)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    prix = models.FloatField()
    quantite = models.IntegerField()
    amenities = models.ManyToManyField(Amenity)
    taille = models.IntegerField()
    note = models.FloatField()
    lit = models.IntegerField()
    date_in = models.DateField()
    date_out = models.DateField()
    remise = models.IntegerField()