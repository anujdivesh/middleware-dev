from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Notice
from .serializers import NoticeSerializer
from .permissions import IsAuthenticatedForPOSTOnly

class NoticeView(viewsets.ModelViewSet):
    # GET is public; POST/PUT/PATCH/DELETE require authentication.
    # Images can be uploaded as multipart/form-data.
    permission_classes = [IsAuthenticatedForPOSTOnly]
    queryset = Notice.objects.all().order_by('id')
    serializer_class = NoticeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_notice_enabled']

    # GET /middleware/api/notice/enabled/ -> all notices with is_notice_enabled=True
    @action(detail=False, methods=['get'])
    def enabled(self, request):
        queryset = self.queryset.filter(is_notice_enabled=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
