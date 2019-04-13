import django_filters

from .models import RentForm


class RentFilter(django_filters.FilterSet):
    class Meta:
        model = RentForm
        fields = ['brand_name', 'username', 'implement', 'Hp', 'city']
