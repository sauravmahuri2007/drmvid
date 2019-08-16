from rest_framework import serializers

from .models import DRMVideo


class DRMVideoSerializer(serializers.ModelSerializer):

    path = serializers.ReadOnlyField(source='video.name')

    class Meta:
        model = DRMVideo
        fields = ('id', 'name', 'video', 'description', 'created_dtm', 'path')

