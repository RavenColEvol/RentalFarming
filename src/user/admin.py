from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from tractor.models import MyImplementation
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import *


class InLineMyImplement(admin.StackedInline):
    model = MyImplementation


class InLineUser(admin.StackedInline):
    model = UserProfile


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # This line will add User Profile along with our user model.
    inlines = (InLineUser,)

    # that reference specific fields on auth.User.
    list_display = ('__str__', 'full_name', 'is_superuser', 'is_renter')
    list_filter = ('is_superuser', 'is_active', 'is_staff', 'is_renter')
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff', 'is_renter',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2')}
         ),
    )
    search_fields = ('phone_number',)
    ordering = ('-date_joined',)
    filter_horizontal = ()

    @staticmethod
    def phone_numbers(obj):  # parameter is an object for accessing the variables.
        if len(str(obj.phone_number)) == 3:
            return obj.phone_number
        normalized_phone_number = '{} {} {}'.format(
            str(obj.phone_number)[:3],
            str(obj.phone_number)[3:6],
            str(obj.phone_number)[6:]
        )
        return normalized_phone_number

    @staticmethod
    def full_name(obj):
        return obj.userprofile.full_name()


admin.site.site_header = 'KH-e-TI Admin Panel'
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
