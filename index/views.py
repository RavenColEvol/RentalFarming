from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView, FormView
from index.models import TractorInfo

from index.forms import OwnerInfo, TractorInfoForm

# Create your views here.
class Index(TemplateView):
    template_name = 'index/index.html'

def rentView(request):
    template_name = 'rent/rent.html'
    form = OwnerInfo()
    if request.method == 'POST':
        form = OwnerInfo(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            redirect('/')
    return render(request,template_name,{'form':form})

def rentView2(request):
    template_name = 'rent/rent-2.html'
    form = TractorInfoForm
    if request.method == 'POST':
        form = TractorInfoForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/')
    return render(request,template_name,{'form':form})

class HireView(ListView):
    model = TractorInfo
    context_object_name = 'tractors'
    template_name = 'rent/hire.html'
    
    