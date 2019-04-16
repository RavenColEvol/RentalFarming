from django import forms
from .models import Tractor

from .models import Implementation


class TractorCreationForm(forms.ModelForm):
    implement = forms.ModelMultipleChoiceField(queryset=Implementation.objects.all(),
                                               widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Tractor
        fields = ['user',
                  'image',
                  'Drive',
                  'Hp',
                  'RentPerHour',
                  'brand_name',
                  'model_name',
                  'implement',
                  'rent_choice',
                  'working_radius',
                  'note',
                  ]
