from rest_framework import serializers
from .models import SubMenu2

class SubMenu2Serializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenu2
        fields = ('__all__') 
        depth = 3