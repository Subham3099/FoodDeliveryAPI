from django.shortcuts import render
from .forms import CalculationForm
from .models import Pricing

def calculate_view(request):
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            zone_v = form.cleaned_data['zone']
            organization_id = form.cleaned_data['organization_id']
            total_distance = form.cleaned_data['total_distance']
            item_type = form.cleaned_data['item_type']
            item_id = form.cleaned_data['item_id']
            
            # Query the Pricing table
            try:
                pricing_info = Pricing.objects.get(type=item_type, organization=organization_id,zone=zone_v)
                base_distance_in_km = pricing_info.base_distance_in_km
                km_price = pricing_info.km_price
                fix_price = pricing_info.fix_price
            except Pricing.DoesNotExist:
                # Handle case when pricing info doesn't exist
                base_distance_in_km = 0
                km_price = 0
                fix_price = 0
            
            # Perform calculations
            value1 =  fix_price + (total_distance-min(base_distance_in_km,total_distance))*km_price
            
            return render(request, 'result.html', {'value1': value1})
    else:
        form = CalculationForm()
    
    return render(request, 'input_form.html', {'form': form})
