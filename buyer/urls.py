from django.urls import path, include
from pomelo.settings import api_settings
from .views import ProfileViewSet


RouterClass = api_settings.DEFAULT_ROUTER
router = RouterClass()
router.register('profile', ProfileViewSet)

urlpatterns = [
    path('', include((router.urls, 'buyer_manage'), namespace='buyer')),
]
