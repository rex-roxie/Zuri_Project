from dataclasses import fields
from django import forms
from .models import Driver

class SearchDriverForm(forms.Form):
    search = forms.CharField(max_length=50, required=False)



class AddDriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'email', 'phone', 'medical_card_number', 'medical_card_expiry_date', 'truck_number', 'driver_license_numbers', 'driver_license_expiry_date', 'certification', 'citizenship']
        
class DeleteDriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'phone']
