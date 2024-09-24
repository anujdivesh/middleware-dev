from rest_framework import serializers
from .models import SubMenu1

class SubMenu1Serializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenu1
        fields = ('__all__') 
        depth = 2