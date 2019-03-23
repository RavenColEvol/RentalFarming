from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, aadhaar_number, password=None, is_active=False):
        if not aadhaar_number:
            raise ValueError("user must have an Aadhaar number")
        if not password:
            raise ValueError('user must have a password')

        user_obj = self.model(aadhaar_number=aadhaar_number)
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        user_obj.active = is_active
        user_obj.admin = False
        user_obj.staff = False

        return user_obj


class User(AbstractBaseUser):
    phone_number = models.IntegerField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    creation_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)  # can login
    password = models.CharField(max_length=999)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']

    objects = UserManager()

    def __str__(self):
        normalized_aadhaar_number = str(
            str(self.phone_number)[:4] + ' ' + str(self.phone_number)[4:8] + ' ' + str(self.phone_number)[8:]
        )
        return normalized_aadhaar_number

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_date_created(self):
        return self.creation_date

    @property
    def is_active(self):
        return self.active
