from datetime import datetime
from django.db import models

# Create your models here.
class Truck(models.Model):
    truck_number = models.CharField(max_length=50)
    driver_assigned_to = models.CharField(max_length=50)
    registration_current_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    registration_expiry_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    inspection_current_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    inspection_expiry_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
