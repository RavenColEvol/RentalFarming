from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, FormView
from index.models import RentForm

from index.forms import HireForm

class Index(TemplateView):
    template_name = 'index/index.html'

def rentView(request):
    template_name = 'rent/rent.html'
    form = HireForm()
    if request.method == 'POST':
        form = HireForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('')
    return render(request,template_name,{'form':form})

# def rentView2(request):
#     template_name = 'rent/rent-2.html'
#     form = TractorInfoForm()
#     if request.method == 'POST':
#         form = TractorInfoForm(request.POST)
#         if form.is_valid():
#             redirect('/rent3')
#     return render(request,template_name,{'form':form})

# def rentView3(request):
#     template_name = 'rent/rent-3.html'
#     form = TractorImage()
#     return render(request,template_name,{'form':form})
#class HireView(ListView):
#    model = RE
#    context_object_name = 'tractors'
#    template_name = 'rent/hire.html'

