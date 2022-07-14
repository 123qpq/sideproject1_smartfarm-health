from rest_framework import serializers
from .models import healthdata

class healthserializer(serializers.ModelSerializer):
    class Meta:
        model = healthdata
        fields = ('user', 'temperature', 'heartrate', 'datetime')
