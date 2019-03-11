from django import forms
from index.models import OwnerInfo
class OwnerInfo(forms.ModelForm):
    class Meta:
        model = OwnerInfo
        fields = '__all__'