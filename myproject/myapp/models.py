from django.db import models

class Organization(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)

class Item(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    type = models.CharField(max_length=10)
    description = models.CharField(max_length=200)

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=10)
    base_distance_in_km = models.IntegerField()
    km_price = models.IntegerField()
    fix_price = models.IntegerField()
