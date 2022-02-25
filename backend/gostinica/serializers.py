from rest_framework import serializers
from .models import Menu,Room

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        field = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'