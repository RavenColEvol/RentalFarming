from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import *


class InLineUser(admin.StackedInline):
    model = UserProfile


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # that reference specific fields on auth.User.
    list_display = ('phone_numbers', 'full_name', 'is_superuser')
    list_filter = ('is_superuser', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser', 'is_staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2')}
         ),
    )
    search_fields = ('phone_number', 'first_name', 'last_name',)
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


admin.site.site_header = 'KH-e-TI Admin Panel'
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
