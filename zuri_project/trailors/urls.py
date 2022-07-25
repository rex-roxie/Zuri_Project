from django.urls import path, include
from trailors.views import trailor_info, trailors_list

urlpatterns = [
    path('', trailors_list, name="trailors"),
    path('trailors/<trailor_id>', trailor_info, name='trailor_info'),
]
