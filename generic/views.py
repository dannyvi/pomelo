from pomelo.decorators import swagger_viewset
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import Image, Video
from .serializers import ImageSerializer, VideoSerializer


@swagger_viewset('图片管理', '图片管理', ['pomelo-常用功能-图片管理'])
class ImageViewSet(ModelViewSet):
    """Image Management Viewset."""
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@swagger_viewset('视频管理', '视频管理', ['pomelo-常用功能-视频管理'])
class VideoViewSet(ModelViewSet):
    """Image Management Viewset."""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

