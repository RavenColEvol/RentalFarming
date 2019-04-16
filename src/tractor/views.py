from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView

from index.decorators import renter_only  # This is not an error
from .models import Tractor
from .forms import TractorCreationForm


class TractorDetailView(DetailView):
    model = Tractor
    template_name = 'tractor/tractor_detail.html'


class MyTractorView(LoginRequiredMixin, ListView):
    model = Tractor
    template_name = 'tractor/my_tractor.html'
    context_object_name = 'tractors'

    @renter_only
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TractorCreateView(LoginRequiredMixin, CreateView):
    model = Tractor
    context_object_name = 'tractors'
    form_class = TractorCreationForm

