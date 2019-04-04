from django import forms
from index.models import RentForm,Profile
from phonenumber_field.modelfields import PhoneNumberField

class HireForm(forms.ModelForm):
    class Meta:
        model = RentForm
        exclude = ('username',)
        

class SignIn(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'