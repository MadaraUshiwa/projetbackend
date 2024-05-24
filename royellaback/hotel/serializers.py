from rest_framework import serializers
from .models import *

class hotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = hotel
        fields = '__all__'