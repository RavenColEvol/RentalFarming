from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import TemplateView
from index import models
from index.filter import RentFilter
from django.contrib.auth.decorators import login_required


import requests
import json

from index.forms import HireForm,SignIn

def index(request):
    rent_list = models.RentForm.objects.all()
    rent_filter = RentFilter(request.GET,queryset=rent_list)
    return render(request,'index/index.html',{'filter':rent_filter})


def rentView(request):
    template_name = 'rent/rent.html'
    form = HireForm()
    if request.method == 'POST':
        form = HireForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('')
    return render(request,template_name,{'form':form})


def search(request):
    rent_list = models.RentForm.objects.all()
    rent_filter = RentFilter(request.GET,queryset=rent_list)
    return render(request,'rent/hire.html',{'filter':rent_filter})

def signIn(request):
    template_name = 'auth/signin.html'
    forms = SignIn()
    if request.method == 'POST':
        form = SignIn(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,template_name,{'forms':forms})

@login_required
def checkout(request,tractor_id):
    template_name = 'rent/tractor_info.html'
    tractor = models.RentForm.objects.get(id=tractor_id)
    rent_per_hour = tractor.RentPerHour
    return render(request,'rent/checkout.html',{'rent':rent_per_hour})

def tractor(request,tractor_id):
    template_name = 'rent/tractor_info.html'
    tractor = models.RentForm.objects.get(id=tractor_id)
    return render(request,template_name,{'tractor':tractor})