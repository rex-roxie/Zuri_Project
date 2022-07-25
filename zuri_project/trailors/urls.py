from django.urls import path, include
from trailors.views import trailor_info, trailors_list, add_trailor, delete_trailor

urlpatterns = [
    path('', trailors_list, name="trailors"),
    path('trailor/<trailor_id>', trailor_info, name='trailor_info'),
    path('add-trailor', add_trailor, name='add_trailor'),
    path('delete-trailor', delete_trailor, name='delete_trailor'),
]
