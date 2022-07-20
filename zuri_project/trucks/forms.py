from django import forms

class SearchTruckForm(forms.Form):
    search = forms.CharField(max_length=50, required=False)