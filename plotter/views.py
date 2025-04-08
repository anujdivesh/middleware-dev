from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from django.shortcuts import get_object_or_404
from .models import Plotter
from .serializers import PlotterSerializer  
from rest_framework.decorators import action
from rest_framework import viewsets
from .permissions import IsAuthenticatedForPOSTOnly
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime

def layer_web_map(request):
    return HttpResponse("Hello world!")

class PlotterView(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedForPOSTOnly] 
    queryset = Plotter.objects.all()

    def list(self, request):
        queryset = Plotter.objects.all()
        serializer = PlotterSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Plotter.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PlotterSerializer(user)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def items_not_done(self, request):
        serializer = PlotterSerializer(self.queryset, many=True)
        return Response(serializer.data)
