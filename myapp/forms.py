from django import forms
from .models import Organization, Item, Pricing

class CalculationForm(forms.Form):
    zone = forms.CharField(max_length=10)
    organization_id = forms.CharField(max_length=20)
    total_distance = forms.FloatField()
    item_type = forms.CharField(max_length=10)

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['id', 'name']
        labels = {
            'id': 'ID',
            'name': 'Name'
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['id', 'type', 'description']
        labels = {
            'id': 'ID',
            'type': 'Type',
            'description': 'Description'
        }

class PricingForm(forms.ModelForm):
    class Meta:
        model = Pricing
        fields = ['organization', 'item', 'zone', 'base_distance_in_km', 'km_price', 'fix_price']
        labels = {
            'organization': 'Organization',
            'item': 'Item',
            'zone': 'Zone',
            'base_distance_in_km': 'Base Distance (km)',
            'km_price': 'Price per km',
            'fix_price': 'Fixed Price'
        }