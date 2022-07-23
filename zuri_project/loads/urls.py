from django.urls import path, include
from .views import load_info, loads_list

urlpatterns = [
    path('loads/', loads_list),
    path('loads/<load_id>', load_info, name='load_info'),
]
