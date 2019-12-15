from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from pomelo.authjwt.validators import UnicodeUsernameValidator, UnicodePhoneValidator


class BaseUser(AbstractUser):

    phone = models.CharField(verbose_name=_('Phone'),
                             validators=[UnicodePhoneValidator()],
                             null=True, default=None, unique=True, max_length=20)
    email = models.EmailField(_('email address'), null=True, unique=True, blank=True, default=None)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and _ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        null=True,
        default=None
    )
    verify = models.CharField('验证码', null=True, default=None, max_length=6)
    REQUIRED_FIELDS = ['email']

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def check_password(self, raw_password):
        return raw_password == self.password