from django import forms

from .models import Tractor


class TractorCreationForm(forms.ModelForm):
    class Meta:
        model = Tractor

        exclude = [
            'user',
        ]

        widgets = {

            'drive': forms.TextInput(
                attrs={'class': 'input', 'type': 'number', }
            ),
            'hp': forms.TextInput(
                attrs={'class': 'input', 'type': 'number', }
            ),
            'rent_per_hour': forms.TextInput(
                attrs={'class': 'input', 'type': 'number', }
            ),
            'brand_name': forms.Select(
                attrs={'class': 'select', }
            ),
            'model_name': forms.TextInput(
                attrs={'class': 'input', }
            ),
            'rent_choice': forms.Select(
                attrs={'class': 'select', }
            ),
            'working_radius': forms.TextInput(
                attrs={'class': 'input', 'type': 'number', }
            ),
            'note': forms.Textarea(
                attrs={'class': 'textarea', }
            ),
        }
