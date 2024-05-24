from rest_framework import serializers
from .models import *

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        
class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'