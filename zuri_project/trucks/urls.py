from django.urls import path, include
from trucks.views import truck_info, trucks_list

urlpatterns = [
    path('trucks/', trucks_list),
    path('trucks/<truck_id>', truck_info, name='truck_info'),
]
