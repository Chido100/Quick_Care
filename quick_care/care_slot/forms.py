from django import forms
from .models import CareSlot


class CareSlotForm(forms.ModelForm):
    class Meta:
        model = CareSlot
        fields = ['number_of_kids', 'age_group', 'additional_care', 'postcode', 'slot_date']
        
