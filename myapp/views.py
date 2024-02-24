from django.shortcuts import render,redirect
from .forms import CalculationForm,OrganizationForm, ItemForm, PricingForm
from .models import Pricing,Organization, Item

def calculate_view(request):
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            zone_v = form.cleaned_data['zone']
            organization_id = form.cleaned_data['organization_id']
            total_distance = form.cleaned_data['total_distance']
            item_type = form.cleaned_data['item_type']
            
            # Query the Pricing table
            try:
                Item_info = Item.objects.get(type=item_type) 
                obitem_id = Item_info.id
                pricing_info = Pricing.objects.get(item_id= obitem_id , organization=organization_id,zone=zone_v)
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

# Organization views
def organization_list(request):
    organizations = Organization.objects.all()
    return render(request, 'organization_list.html', {'organizations': organizations})

def organization_create(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organization_list')
    else:
        form = OrganizationForm()
    return render(request, 'organization_form.html', {'form': form})

# Item views
def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})

# Pricing views
def pricing_list(request):
    pricings = Pricing.objects.all()
    return render(request, 'pricing_list.html', {'pricings': pricings})

def pricing_create(request):
    if request.method == 'POST':
        form = PricingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pricing_list')
    else:
        form = PricingForm()
    return render(request, 'pricing_form.html', {'form': form})

