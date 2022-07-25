from django.urls import path, include
from .views import add_load, load_info, loads_list, delete_load

urlpatterns = [
    path('', loads_list, name="loads"),
    path('loads/<load_id>', load_info, name='load_info'),
    path('add-load', add_load, name='add_load'),
    path('delete-load', delete_load, name='delete_load'),
]
