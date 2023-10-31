from django import forms
from .models import ChildMinderKYC


class ChildMinderForm(forms.ModelForm):
    class Meta:
        model = ChildMinderKYC
        fields = [
            'first_name', 'last_name', 'gender', 'photograph', 'phone_number', 'city', 'post_code', 'house_number',
            'number_of_occupants', 'identity_type', 'identity_image', 'child_minder_training', 'dbs_criminal_record_check',
            'child_care_register', 'home_risk_assessment'
        ]
