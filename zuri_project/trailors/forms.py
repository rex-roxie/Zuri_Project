from django import forms

class SearchTrailorForm(forms.Form):
    search = forms.CharField(max_length=50, required=False)