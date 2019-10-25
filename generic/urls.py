from django.urls import path, include
from pomelo.settings import api_settings
from .views import ImageViewSet, VideoViewSet


RouterClass = api_settings.DEFAULT_ROUTER
router = RouterClass()
router.register('image', ImageViewSet)
router.register('video', VideoViewSet)

urlpatterns = [
    path('', include((router.urls, 'pomelo'), namespace='pomelo')),
]
