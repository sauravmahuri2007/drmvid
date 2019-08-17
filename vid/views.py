from rest_framework import permissions
from rest_framework import viewsets
from video_encoding.models import Format

from .models import DRMVideo
from .serializers import DRMVideoSerializer, FormatVideoSerializer


class DRMVideoView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DRMVideoSerializer
    queryset = DRMVideo.objects.all()


class FormatVideoView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FormatVideoSerializer
    queryset = Format.objects.all()
