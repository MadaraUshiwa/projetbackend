from rest_framework import serializers
from .models import *

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'        