from django import forms

class SearchDriverForm(forms.Form):
    search = forms.CharField(max_length=50, required=False)