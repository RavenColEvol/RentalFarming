from django.views.generic import DetailView, ListView

from src.index.decorators import renter_only  # This is not an error
from .models import Tractor


class TractorDetailView(DetailView):
    model = Tractor
    template_name = 'tractor/detail.html'


class MyTractorView(ListView):
    model = Tractor
    template_name = 'tractor/my_tractor.html'
    context_object_name = 'tractors'

    @renter_only
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
