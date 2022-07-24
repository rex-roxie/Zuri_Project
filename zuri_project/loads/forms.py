from django import forms

from loads.models import Load

class SearchLoadForm(forms.Form):
    search = forms.CharField(max_length=50, required=False)

class AddLoadForm(forms.ModelForm):
    class Meta:
        model = Load
        fields = ['load_number', 'driver_assigned_to', 'pickup_date', 'pickup_location', 'dropoff_location']
        
class DeleteLoadForm(forms.ModelForm):
    class Meta:
        model = Load
        fields = ['load_number']
