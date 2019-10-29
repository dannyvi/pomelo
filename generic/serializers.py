from rest_framework import serializers
from .models import Image, Video


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        request = self.context.get('request')
        url = ret['url']
        ret['url'] = request.build_absolute_uri(url)
        return ret


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"
