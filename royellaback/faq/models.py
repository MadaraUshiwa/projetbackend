from django.db import models

# Create your models here.

class Faq(models.Model):
    question = models.CharField(max_length=100)
    response = models.CharField(max_length=200)
    active = models.BooleanField(default=False)