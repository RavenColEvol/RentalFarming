from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView
from index.models import TractorInfo

from index.forms import OwnerInfo

# Create your views here.
class Index(TemplateView):
    template_name = 'index/index.html'

class RentView(FormView):
    form_class = OwnerInfo
    success_url = '/'
    template_name = 'rent/rent.html'

class HireView(ListView):
    model = TractorInfo
    context_object_name = 'tractors'
    template_name = 'rent/hire.html'