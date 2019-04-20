from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from index.decorators import renter_only
from .forms import TractorCreationForm
from .models import Tractor


# stripe.api_key = settings.STRIPE_SECRET


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

    def form_valid(self, form):
        tractor = form.save(commit=False)

        # clean data
        tractor.user = self.request.user
        tractor.save()

        messages.success(self.request, str(tractor) + ' is added')

        return redirect('tractor:my_tractor')


class TractorUpdateView(LoginRequiredMixin, UpdateView):
    model = Tractor
    form_class = TractorCreationForm
    context_object_name = 'tractors'


class TractorDeleteView(LoginRequiredMixin, DeleteView):
    model = Tractor
    success_url = reverse_lazy('tractor:my_tractor')


class Checkout(LoginRequiredMixin, View):
    template_name = 'tractor/checkout.html'
