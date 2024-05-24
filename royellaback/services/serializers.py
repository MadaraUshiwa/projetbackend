from rest_framework import serializers
from .models import *

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
        
        