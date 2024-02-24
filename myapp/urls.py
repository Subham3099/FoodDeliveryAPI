from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('calculate/', views.calculate_view, name='calculate'),  # Correct view import

    # Organization URLs
    path('organizations/', views.organization_list, name='organization_list'),
    path('organizations/create/', views.organization_create, name='organization_create'),
    # Add URL patterns for updating and deleting organizations if needed

    # Item URLs
    path('items/', views.item_list, name='item_list'),
    path('items/create/', views.item_create, name='item_create'),
    # Add URL patterns for updating and deleting items if needed

    # Pricing URLs
    path('pricings/', views.pricing_list, name='pricing_list'),
    path('pricings/create/', views.pricing_create, name='pricing_create'),
    # Add URL patterns for updating and deleting pricings if needed
]
