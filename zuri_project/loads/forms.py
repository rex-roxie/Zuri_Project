from django import forms

class SearchLoadForm(forms.Form):
    search = forms.CharField(max_length=50, required=False)