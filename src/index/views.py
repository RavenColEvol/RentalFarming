from django.shortcuts import render, redirect
from django.views.generic import ListView

from tractor.models import Tractor
from .filter import RentFilter
from .forms import HireForm, SignIn
from .models import RentForm


class IndexView(ListView):
    model = Tractor
    template_name = 'index/index.html'
    context_object_name = 'tractors'


def rent_view(request):
    template_name = 'rent/rent.html'
    form = HireForm()
    if request.method == 'POST':
        form = HireForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('')
    return render(request, template_name, {'form': form})


def search_view(request):
    rent_list = RentForm.objects.all()
    rent_filter = RentFilter(request.GET, queryset=rent_list)
    return render(request, 'rent/hire.html', {'filter': rent_filter})


def signin_view(request):
    template_name = 'auth/signin.html'
    forms = SignIn()
    if request.method == 'POST':
        form = SignIn(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, template_name, {'forms': forms})
