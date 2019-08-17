from rest_framework import serializers
from video_encoding.models import Format, VideoField

from .models import DRMVideo


class FormatVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Format
        fields = ('__all__')


class DRMVideoSerializer(serializers.ModelSerializer):

    path = serializers.ReadOnlyField(source='video.name')
    format_set = FormatVideoSerializer(read_only=True, many=True)

    class Meta:
        model = DRMVideo
        fields = ('__all__')