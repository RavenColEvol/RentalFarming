from django import forms
from index.models import OwnerInfo, TractorInfoForm
from phonenumber_field.modelfields import PhoneNumberField


class OwnerInfo(forms.ModelForm):
    class Meta:
        model = OwnerInfo
        fields = '__all__'
        widgets = {
            'username':forms.TextInput(attrs={
                'class':'input',
                'placeholder':'e.g. Sachin Tendulkar'
            }),
            'email':forms.EmailInput(attrs={
                'class':'input',
                'placeholder':'e.g. sachin@gmail.com'
            }),
            'number':forms.NumberInput(attrs={
                'class':'input',
                'placeholder':'+91'
            }),
            'pincode':forms.NumberInput(attrs={
                'class':'input',
                'placeholder':'401105'
            }),
            'address':forms.Textarea(attrs={
                'class':'input',
                'rows':3
            }),
            'state':forms.Select(attrs={
                'class':'input',
            }),
            'city':forms.Select(attrs={
                'class':'input',
            }),
            
        }


class TractorInfoForm(forms.ModelForm):
    class Meta:
        model = TractorInfoForm
        fields = '__all__' 
