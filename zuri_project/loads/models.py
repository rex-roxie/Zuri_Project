from datetime import datetime
from django.db import models

# Create your models here.
class Load(models.Model):
    load_number = models.CharField(max_length=50)
    driver_assigned_to = models.CharField(max_length=50)
    pickup_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    pickup_location = models.CharField(max_length=50)
    dropoff_location = models.CharField(max_length=50)
