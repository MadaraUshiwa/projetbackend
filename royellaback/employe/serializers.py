from rest_framework import serializers
from .models import *

class employeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'