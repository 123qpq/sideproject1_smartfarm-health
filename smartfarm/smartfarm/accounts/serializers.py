from rest_framework import serializers
from .models import account

class accountserializer(serializers.ModelSerializer):
    class Meta:
        model = account
        fields = ('username', 'pwd')
