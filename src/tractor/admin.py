from django.contrib import admin

from .models import Tractor, Implementation, MyImplementation

admin.site.register(Tractor)
admin.site.register(Implementation)
admin.site.register(MyImplementation)
