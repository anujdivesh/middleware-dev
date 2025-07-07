from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Widget
from .serializers import WidgetSerializer
from .permissions import IsAuthenticatedForPOSTOnly
from django_filters.rest_framework import DjangoFilterBackend
from .filters import WidgetFilter

def submenu_1(request):
    return HttpResponse("Hello world!")

class WidgetView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedForPOSTOnly]
    queryset = Widget.objects.all().order_by('id')
    serializer_class = WidgetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = WidgetFilter

    def list(self, request):
        queryset = self.queryset

        # Show all unrestricted widgets to anyone
        unrestricted_widgets = queryset.filter(is_restricted=False)

        # For restricted widgets, only show if user is authenticated and country matches
        restricted_widgets = queryset.filter(is_restricted=True)
        allowed_restricted_widgets = Widget.objects.none()
        if request.user.is_authenticated:
            try:
                user_country_id = request.user.account.country.id
                allowed_restricted_widgets = restricted_widgets.filter(country_id=user_country_id)
            except AttributeError:
                # If user has no country, don't show restricted widgets
                allowed_restricted_widgets = Widget.objects.none()
        # Combine the two querysets
        final_queryset = unrestricted_widgets | allowed_restricted_widgets
        # Optionally apply filter backends (for filtering by country etc)
        final_queryset = self.filter_queryset(final_queryset)

        serializer = WidgetSerializer(final_queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        widget = get_object_or_404(Widget, pk=pk)
        # Unrestricted: anyone can retrieve
        if not widget.is_restricted:
            serializer = WidgetSerializer(widget)
            return Response(serializer.data)
        # Restricted: check auth and country
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            user_country_id = request.user.account.country.id
        except AttributeError:
            return Response({"detail": "Your account does not have a country set."}, status=status.HTTP_400_BAD_REQUEST)
        if widget.country_id != user_country_id:
            return Response({"detail": "You are not allowed to access this widget."}, status=status.HTTP_403_FORBIDDEN)
        serializer = WidgetSerializer(widget)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def items_not_done(self, request):
        # Placeholder action, implement logic as needed
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = WidgetSerializer(self.queryset, many=True)
        return Response(serializer.data)