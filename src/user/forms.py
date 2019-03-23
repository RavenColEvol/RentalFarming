from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='confirm password')

    class Meta:
        model = User
        fields = ['phone_number', 'first_name', 'last_name', 'password1', 'password2']


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone_number', 'first_name', 'last_name')

    # def clean_phone_number(self):
    #     phone_number = self.cleaned_data['phone_number']
    #     print(phone_number)
    #     return '+91' + str(phone_number)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('phone_number', 'password', 'active')

    def clean_password(self):
        return self.initial["password"]
