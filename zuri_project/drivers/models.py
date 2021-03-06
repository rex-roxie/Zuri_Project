from datetime import date
import numbers
from django.db import models
 # Hazard, tanker_endorsement

certification_options = (
    ('hazard', 'Hazard'),
    ('tanker_endorsement', 'Tanker Endorsement'),
    ('both', 'Both Hazard and Tanker Endorsement'),
    ('neither', 'Neither')
)

# PR stands for permanent resident

citizenship_options = (
    ('citizen', 'C (citizen)'),
    ('non_citizen', 'PR (permanent residence)'),
    ('work_permit', 'WP (work permit)')
)


# Create your models here.
class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50, default=None)
    medical_card_number = models.CharField(max_length=50)
    medical_card_expiry_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    truck_number = models.CharField(max_length=50)
    driver_license_numbers = models.CharField(max_length=50)
    driver_license_expiry_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    certification = models.CharField(max_length=50, choices=certification_options)
    citizenship = models.CharField(max_length=50, choices=citizenship_options)

    def __str__(self):
        return self.first_name