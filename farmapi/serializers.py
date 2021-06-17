from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import farmdata, farminfo

class farmserializer(serializers.ModelSerializer):
    class Meta:
        model = farmdata
        fields = ('farmid', 'moisture', 'temperature', 'humidity', 'barometric', 'altitude', 'datetime')

class checkserializer(serializers.ModelSerializer):
    class Meta:
        model = farminfo
        fields = ('farmid', 'toggle')
