from datetime import datetime
from django.db import models

# Create your models here.
class Trailor(models.Model):
    trailor_number = models.CharField(max_length=50)
    driver_assigned_to = models.CharField(max_length=50)
    registration_current_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    registration_expiry_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    inspection_current_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    inspection_expiry_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    vin_number = models.CharField(max_length=50, default=None)
    manufacturer_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, default=None)
    vented = models.BooleanField(default=False)