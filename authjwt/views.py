from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from .serializers import BaseUserSerializer, UserNameSerializer
# from rest_framework.permissions import IsAdminUser
from rest_framework import permissions
from rest_framework.decorators import action
from pomelo.serializers import PasswordSerializer
from pomelo.permissions import IsUserInstance
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.utils.decorators import method_decorator

UserModel = get_user_model()

test_param = openapi.Parameter('search',
                               openapi.IN_QUERY,
                               description=_('search email | phone '),
                               type=openapi.TYPE_STRING)
user_response = openapi.Response(_('User infomation'), UserNameSerializer)


@method_decorator(name='list',
                  decorator=swagger_auto_schema(
                      operation_description=_('Only Admin User can get User list.'),
                      tags=['用户登录'],
                      responses={'200': BaseUserSerializer(many=True)}))
@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_description=_('Create new user.'),
    request_body=openapi.Schema(
        title=_('Create'),
        type=openapi.TYPE_OBJECT,
        required=['password', ],
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'phone': openapi.Schema(type=openapi.TYPE_STRING),
            'password': openapi.Schema(type=openapi.TYPE_STRING,  description=_('At least one of email|phone field.'))
    }),
    responses={'200': BaseUserSerializer},
    tags=['用户登录']
))
@method_decorator(name='retrieve',
                  decorator=swagger_auto_schema(
                      operation_description=_('Get User infomation. \n Permissions: Is Owner.'),
                      tags=['用户登录']
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_description=_('Update user info.\n Permissions: Is Owner.'),
    tags=['用户登录'],
    request_body=openapi.Schema(
        title=_('BaseUser'),
        type=openapi.TYPE_OBJECT,
        required=['password', ],
        properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'phone': openapi.Schema(type=openapi.TYPE_STRING, description=_('Anyone or both.'))
        }
    ),
    responses={'200': BaseUserSerializer}
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_description=_('Delete user.'),tags=['用户登录']))
class BaseUserViewset(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = UserModel.objects.all()
    serializer_class = BaseUserSerializer

    def get_permissions(self):
        """
        Allow anyone to sign up.
        AdminUser can query user list.
        Owner can edit itself.
        """
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        elif self.action == 'list':
            permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated, IsUserInstance]
        return [permission() for permission in permission_classes]

    @swagger_auto_schema(method='post', operation_description=_('set password'), tags=['用户登录', '买家'])
    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
