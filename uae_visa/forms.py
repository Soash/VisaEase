from django import forms
from uae_visa.models import *


class VisaInfoForm(forms.ModelForm):
    class Meta:
        model = VisaInfo
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        for field in cleaned_data:
            if cleaned_data[field] is None:
                cleaned_data[field] = ''
        return cleaned_data
    

class VisaApplicationForm(forms.ModelForm):
    class Meta:
        model = VisaApplication
        exclude = ['serial_no', 'visa_info']
    
    def clean(self):
        cleaned_data = super().clean()
        for field in cleaned_data:
            if cleaned_data[field] is None:
                cleaned_data[field] = ''
        return cleaned_data