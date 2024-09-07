from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from django.shortcuts import get_object_or_404
from .models import SubMenu2
from .serializers import SubMenu2Serializer  
from rest_framework.decorators import action
from rest_framework import viewsets
from .permissions import IsAuthenticatedForPOSTOnly
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime

def submenu_2(request):
    return HttpResponse("Hello world!")

class SubMenu2View(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedForPOSTOnly] 
    queryset = SubMenu2.objects.all()

    def list(self, request):
        queryset = SubMenu2.objects.all()
        serializer = SubMenu2Serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = SubMenu2.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = SubMenu2Serializer(user)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def items_not_done(self, request):
        serializer = SubMenu2Serializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SubMenu2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Object successfully created."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        queryset = SubMenu2.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = SubMenu2Serializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Object successfully updated."},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = SubMenu2.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        item.delete()
        return Response({"detail": "Object successfully deleted."},status=status.HTTP_200_OK)