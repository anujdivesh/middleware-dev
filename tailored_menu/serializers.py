from rest_framework import serializers
from .models import TailoredMenu

class TailoredMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = TailoredMenu
        fields = ('__all__') 
        depth = 2