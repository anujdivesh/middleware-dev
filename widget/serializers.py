from rest_framework import serializers
from .models import Widget

class WidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Widget
        fields = ('__all__') 
        depth = 1