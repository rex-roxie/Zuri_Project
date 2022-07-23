from django.urls import path, include
from .views import driver_info, drivers_list, add_driver, delete_driver

urlpatterns = [
    path('', drivers_list, name="drivers"),
    path('<driver_id>', driver_info, name='driver_info'),
    path('add-driver', add_driver, name='add_driver'),
    path('delete-driver', delete_driver, name='delete_driver'),
]
