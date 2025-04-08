from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from django.shortcuts import get_object_or_404
from .models import DataType
from .serializers import DataTypeSerializer  
from rest_framework.decorators import action
from rest_framework import viewsets
from .permissions import IsAuthenticatedForPOSTOnly


def data_type(request):
    return HttpResponse("Hello world!")

class DataTypeView(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedForPOSTOnly] 
    queryset = DataType.objects.all()

    def list(self, request):
        queryset = DataType.objects.all()
        serializer = DataTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = DataType.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DataTypeSerializer(user)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def items_not_done(self, request):
        serializer = DataTypeSerializer(self.queryset, many=True)
        return Response(serializer.data)
