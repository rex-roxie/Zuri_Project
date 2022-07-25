from django import forms

from trucks.models import Truck

class SearchTruckForm(forms.Form):
    search = forms.CharField(max_length=50, required=False)

class AddTruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields = ['truck_number', 'driver_assigned_to', 'registration_current_date', 'registration_expiry_date', 'inspection_current_date', 'inspection_expiry_date', 'vin_number']
        
class DeleteTruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields = ['truck_number']
