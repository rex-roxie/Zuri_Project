from datetime import date
import numbers
from string import capwords
from django.db import models
 # Hazard, tanker_endorsement

certification_options = (
    ('hazard', 'Hazard'),
    ('tanker_endorsement', 'Tanker Endorsement'),
    ('both', 'Both Hazard and Tanker Endorsement'),
    ('neither', 'Neither')
)


# Create your models here.
class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    medical_card_number = models.CharField(max_length=50)
    medical_card_expiry_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    truck_number = models.IntegerField()
    driver_license_numbers = models.IntegerField()
    driver_license_expiry_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    certification = models.CharField(max_length=50, choices=certification_options)