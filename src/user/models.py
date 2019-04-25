from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _

from .validators import phone_number_length_validator


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, password, **extra_fields):
        """
        Creates and saves a User with the given phone_number and password.
        """
        if not phone_number:
            raise ValueError('The given phone_number must be set')
        phone_number = phone_number
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_seller_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_renter', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(_('phone number'),
                                    unique=True, max_length=10,
                                    validators=[phone_number_length_validator, ], )

    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_superuser = models.BooleanField(_('admin'), default=False)
    is_renter = models.BooleanField(_('Renter'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        if len(str(self.phone_number)) == 3:
            return self.phone_number
        normalized_phone_number = '{} {} {}'.format(
            str(self.phone_number)[:3],
            str(self.phone_number)[3:6],
            str(self.phone_number)[6:]
        )
        return normalized_phone_number


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'))
    profile_pic = models.ImageField(_('Profile Picture'), upload_to="media/", null=True, blank=True)

    first_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=100)

    address = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')

    def __str__(self):
        return str(self.user)

    def full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return str(full_name.strip())

    def get_short_name(self):
        return self.first_name


def create_profile(instance, **kwargs):
    if kwargs['created']:
        UserProfile.objects.create(user=instance)


post_save.connect(receiver=create_profile, sender=User)
