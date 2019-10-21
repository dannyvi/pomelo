import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class ASCIIUsernameValidator(validators.RegexValidator):
    regex = r'^[\w]+$'
    message = _(
        'Enter a valid username. This value may contain only English letters, '
        'numbers, and _ characters.'
    )
    flags = re.ASCII


@deconstructible
class UnicodeUsernameValidator(validators.RegexValidator):
    regex = r'^[\w]+$'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, and _ characters.'
    )
    flags = 0

@deconstructible
class UnicodeEmailValidator(validators.RegexValidator):
    regex = r'^[\w.@+-]+$'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, and @/./+/-/_ characters.'
    )
    flags = 0
    
@deconstructible
class UnicodePhoneValidator(validators.RegexValidator):
    regex = r'^[\d]+$'
    message = _(
        'Enter a valid phone number. This value may contain only digits. '
    )
    flags = 0