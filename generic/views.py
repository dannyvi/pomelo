from pomelo.decorators import swagger_viewset
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from django.utils.translation import gettext_lazy as _
from .models import Image, Video
from .serializers import ImageSerializer, VideoSerializer
from drf_yasg import openapi
from django.utils.decorators import method_decorator as md
from drf_yasg.utils import swagger_auto_schema as sas
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser


@md(name='create',
    decorator=sas(
        manual_parameters=[openapi.Parameter('url',
                                             openapi.IN_FORM,
                                             description=_('Upload image.'),
                                             type=openapi.TYPE_FILE), ],
        tags=['图片上传']))
@parser_classes([MultiPartParser, ])
class ImageViewSet(ModelViewSet):
    """Image Management Viewset."""
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



@md(name='create',
    decorator=sas(
        manual_parameters=[openapi.Parameter('url',
                                             openapi.IN_FORM,
                                             description='上传视频',
                                             type=openapi.TYPE_FILE), ],
        tags=['视频上传']))
@parser_classes([MultiPartParser, ])
class VideoViewSet(ModelViewSet):
    """Image Management Viewset."""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

