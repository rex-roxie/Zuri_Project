from django import forms

from trailors.models import Trailor

class SearchTrailorForm(forms.Form):
    search = forms.CharField(max_length=50, required=False)

class AddTrailorForm(forms.ModelForm):
    class Meta:
        model = Trailor
        fields = ['trailor_number', 'driver_assigned_to', 'registration_current_date', 'registration_expiry_date', 'inspection_current_date', 'inspection_expiry_date', 'vin_number', 'manufacturer_date', 'vented']
        
class DeleteTrailorForm(forms.ModelForm):
    class Meta:
        model = Trailor
        fields = ['trailor_number']
