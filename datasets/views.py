from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from django.shortcuts import get_object_or_404
from .models import Dataset
from .serializers import DatasetSerializer  
from rest_framework.decorators import action
from rest_framework import viewsets
from .permissions import IsAuthenticatedForPOSTOnly


def datasets(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())
  
class DatasetView(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedForPOSTOnly] 
    queryset = Dataset.objects.all()

    def list(self, request):
        queryset = Dataset.objects.all()
        serializer = DatasetSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Dataset.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DatasetSerializer(user)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def items_not_done(self, request):
        serializer = DatasetSerializer(self.queryset, many=True)
        return Response(serializer.data)
