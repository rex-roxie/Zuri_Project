from django.urls import path, include
from trucks.views import truck_info, trucks_list, add_truck, delete_truck

urlpatterns = [
    path('', trucks_list, name="trucks"),
    path('truck/<truck_id>', truck_info, name='truck_info'),
    path('add-truck', add_truck, name='add_truck'),
    path('delete-truck', delete_truck, name='delete_truck'),
]
