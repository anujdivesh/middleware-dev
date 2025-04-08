from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from django.shortcuts import get_object_or_404
from .models import TailoredMenu
from .serializers import TailoredMenuSerializer  
from rest_framework.decorators import action
from rest_framework import viewsets
from .permissions import IsAuthenticatedForPOSTOnly
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TailoredMenuFilter

def submenu_1(request):
    return HttpResponse("Hello world!")

class TailoredMenuView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedForPOSTOnly] 
    queryset = TailoredMenu.objects.all().order_by('id')
    serializer_class = TailoredMenuSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TailoredMenuFilter  # Make sure to include the fields you want to filter

    def list(self, request):
        # Print the query parameters to check what we're filtering by
        if not request.query_params:
            return Response(
                {"detail": "You must provide a filter to view the menu."},
                status=status.HTTP_403_FORBIDDEN
            )
        

        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            user_country_id = request.user.account.country.id  # Access the user's country ID
        except AttributeError:
            return Response({"detail": "Your account does not have a country set."}, status=status.HTTP_400_BAD_REQUEST)

        country_filter = request.query_params.get('country_id', None)

        # If a country filter is provided, ensure it matches the user's country
        if country_filter and int(country_filter) != user_country_id:
            return Response(
                {"detail": "You are not allowed to filter by a country other than your own."},
                status=status.HTTP_403_FORBIDDEN
            )
        # Apply filters to the queryset
        queryset = self.filter_queryset(self.queryset)


        serializer = TailoredMenuSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)
            
        queryset = TailoredMenu.objects.all().order_by('id')
        user = get_object_or_404(queryset, pk=pk)
        serializer = TailoredMenuSerializer(user)
        return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['get'])
    def items_not_done(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = TailoredMenuSerializer(self.queryset, many=True)
        return Response(serializer.data)
