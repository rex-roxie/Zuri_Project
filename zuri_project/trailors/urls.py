from django.urls import path, include
from trailors.views import trailor_info, trailors_list

urlpatterns = [
    path('', trailors_list),
    path('trailors/<trailor_id>', trailor_info, name='trailor_info'),
]
