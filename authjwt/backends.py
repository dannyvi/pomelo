
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import Permission
from django.utils.deprecation import RemovedInDjango31Warning

UserModel = get_user_model()


class MultiFieldLoginModelBackend(ModelBackend):
    """supports email, phone, username login"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        print(username, kwargs)
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if '@' in username:
            kwargs = {'email': username}
        elif username.isdigit():
            kwargs = {'phone': username}
        else:
            kwargs = {'username': username}
        try:
            user = UserModel._default_manager.get(**kwargs) #get_by_natural_key(**kwargs)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def has_perm(self, user_obj, perm, obj):
        """We don't configure permissions here."""
        return None