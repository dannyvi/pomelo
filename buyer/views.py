from rest_framework.viewsets import ModelViewSet
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import permissions
from ..permissions import IsOwnerOrReadOnly
from ..decorators import swagger_viewset
from django.utils.translation import gettext_lazy as _

@swagger_viewset(
    _('User-Profile'),
    _('Buyer profile entry.\n'
      '`list`method provide all profiles for **Admin**,'
      ' and one for **Buyer**.\n'
      'Admin User has all permissions.\n'
      'Buyer User has **object permission** for his own profile.'))
class ProfileViewSet(ModelViewSet):
    """Buyer profile entry.

    The `list` method provide profile of all members for **Admin User**, and
    provide one profile for the **Buyer User** of himself.

    The Admin User has all permissions for all profiles.
    The Buyer User has **object permission** for his own profile.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        """
        Allow anyone to sign up.
        AdminUser can query user list.
        Owner can edit itself.
        """
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Profile.objects.all()
        else:
            return Profile.objects.filter(owner=self.request.user)
