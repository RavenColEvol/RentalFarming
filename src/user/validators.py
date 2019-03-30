from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from src.seproject import settings


def phone_number_length_validator(value):
    if not str(value).isdigit() or not len(str(value)) == 10:
        raise ValidationError(_('Phone number is not valid'))


def phone_number_length_login_validator(value):
    if not str(value).isdigit():
        raise ValidationError(_('Phone number is not valid22'))

    if settings.DEBUG:
        if not 3 <= len(str(value)) <= 10:
            raise ValidationError(_('Phone number is not valid33'))
    else:
        if not len(str(value)) == 10:
            raise ValidationError(_('Phone number is not valid44'))
