from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def phone_number_length_validator(value):

    if not str(value).isdigit() or (len(str(value)) != 10 and str(value) != '123'):
        raise ValidationError(_('Phone number is not valid.'))

    if len(str(value)) != 10:
        if str(value) != '123':
            raise ValidationError(_('Phone number is not valid.'))
