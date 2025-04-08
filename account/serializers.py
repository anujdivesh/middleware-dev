from rest_framework import serializers
from .models import Account
from django.contrib.auth.models import User
from country.models import Country

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('__all__') 
        depth = 1