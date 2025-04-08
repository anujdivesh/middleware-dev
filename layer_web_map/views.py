from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import LayerWebMap
from .serializers import LayerWebMapSerializer
from rest_framework.decorators import action
from rest_framework import viewsets
from .permissions import IsAuthenticatedForPOSTOnly

class LayerWebMapView(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedForPOSTOnly]
    queryset = LayerWebMap.objects.all()

    def list(self, request):
        if request.user.is_authenticated:
            # If the user is authenticated, allow access to restricted=True items
            queryset = LayerWebMap.objects.filter(restricted=True)
        else:
            # If the user is not authenticated, only return items where restricted=False
            queryset = LayerWebMap.objects.filter(restricted=False)

        serializer = LayerWebMapSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # Similarly, check if the user is authenticated
        if request.user.is_authenticated:
            queryset = LayerWebMap.objects.all()  # Include all items, since the user is authenticated
        else:
            queryset = LayerWebMap.objects.filter(restricted=False)  # Only return non-restricted items

        user = get_object_or_404(queryset, pk=pk)
        serializer = LayerWebMapSerializer(user)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def items_not_done(self, request):
        if request.user.is_authenticated:
            queryset = LayerWebMap.objects.filter(restricted=True)  # Only restricted items for authenticated users
        else:
            queryset = LayerWebMap.objects.filter(restricted=False)  # Only non-restricted for unauthenticated users

        serializer = LayerWebMapSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = LayerWebMapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Object successfully created."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)
        queryset = LayerWebMap.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = LayerWebMapSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Object successfully updated."},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
