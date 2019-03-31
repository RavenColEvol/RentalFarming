from index.models import RentForm
import django_filters

class RentFilter(django_filters.FilterSet):
    class Meta:
        model = RentForm
        fields = ['brand_name','username','implement','Hp','city']
        