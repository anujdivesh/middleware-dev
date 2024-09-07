from rest_framework import serializers
from .models import SubMenu3

class SubMenu3Serializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenu3
        fields = ('__all__') 
        depth = 2