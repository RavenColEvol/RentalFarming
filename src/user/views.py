from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import *


class UserRegistrationFormView(View):
    form_class = UserRegistrationForm
    template_name = 'user/register.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned data
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(phone_number=phone_number, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('index:index')

        return render(request, self.template_name, {'form': form})


def login_view(request):
    return render(request, 'user/login.html', {})


def logout_view(request):
    logout(request)
    return render(request, 'user/login.html', {})
