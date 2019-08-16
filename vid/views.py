from rest_framework import permissions
from rest_framework import viewsets

from .models import DRMVideo
from .serializers import DRMVideoSerializer


class DRMVideoView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DRMVideoSerializer
    queryset = DRMVideo.objects.all()
