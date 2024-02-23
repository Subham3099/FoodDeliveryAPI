from django import forms

class CalculationForm(forms.Form):
    zone = forms.CharField(max_length=10)
    organization_id = forms.CharField(max_length=20)
    total_distance = forms.FloatField()
    item_type = forms.CharField(max_length=10)
    item_id = forms.CharField(max_length=10)
