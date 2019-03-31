from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from .forms import UserRegistrationForm, UserLoginForm


class UserRegistrationFormView(View):
    form_class = UserRegistrationForm
    template_name = 'user/registration_form.html'

    def get(self, request):
        if request.user.is_authenticated:
            if request.user.get_short_name():
                messages.error(request, 'YOU ARE ALREADY LOGGED IN AS ' + request.user.get_short_name().upper())
            else:
                messages.error(request, 'YOU ARE ALREADY LOGGED IN')
            return redirect('/')
        else:
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # clean data
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password2']
            user.set_password(password)
            user.save()

            messages.success(request, 'Your account has been created.')

            # following line is for log in the user
            user = authenticate(phone_number=phone_number, password=password)

            if user is not None:
                login(request, user)
                if user.is_active:
                    return redirect('index')

        return render(request, self.template_name, {'form': form})


class UserLoginFormView(View):
    form_class = UserLoginForm
    template_name = 'user/login_form.html'

    def get(self, request):
        if request.user.is_authenticated:
            if request.user.get_short_name():
                messages.error(request, 'YOU ARE ALREADY LOGGED IN AS ' + request.user.get_short_name().upper())
            else:
                messages.error(request, 'YOU ARE ALREADY LOGGED IN')
            return redirect('/')
        else:
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            password = form.cleaned_data.get('password')

            user = authenticate(phone_number=phone_number, password=password)
            login(request, user)

            if user.first_name:
                messages.success(request, 'Welcome back, ' + user.get_full_name())

            else:
                messages.success(request, 'Welcome back, User') 
            return redirect('/')

        return render(request, self.template_name, {'form': form})


class UserLogoutVIew(View):

    @staticmethod
    def get(request):

        # This prevent users to manually enter the logout link
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, 'YOU ARE SUCCESSFULLY LOGGED OUT')

        else:
            messages.warning(request, 'NO USER IS CURRENTLY LOGGED IN!')
        return redirect('/')


class ForgetPasswordFormView(View):
    template_name = 'user/forget_password.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
