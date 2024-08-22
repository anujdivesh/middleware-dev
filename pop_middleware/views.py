from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from django.shortcuts import get_object_or_404

def nav(request):
    items = [
        {'title': 'Wavewatch 3 forecast', 'content': 'Content for the first accordion item.'},
        {'title': 'Salinity Forecast', 'content': 'Content for the second accordion item.'},
        {'title': 'PH Forecast', 'content': 'Content for the third accordion item.'},
        
    ]
    return render(request, 'navbar.html', {'items': items})