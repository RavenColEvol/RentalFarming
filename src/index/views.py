from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import HireForm


class Index(TemplateView):
    template_name = 'index/index.html'


def rent_view(request):
    template_name = 'rent/rent.html'
    form = HireForm()
    if request.method == 'POST':
        form = HireForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('')
    return render(request, template_name, {'form': form})
