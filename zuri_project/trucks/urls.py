from django.urls import path, include
from trucks.views import truck_info, trucks_list

urlpatterns = [
    path('', trucks_list, name="trucks"),
    path('trucks/<truck_id>', truck_info, name='truck_info'),
]
