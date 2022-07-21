"""zuri_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from authentication.views import index
from drivers.views import driver_info, drivers_list, add_driver
from trucks.views import truck_info, trucks_list
from trailors.views import trailor_info, trailors_list
from loads.views import load_info, loads_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('', include('django.contrib.auth.urls')),
    path('drivers/', drivers_list, name="drivers"),
    path('driver/<driver_id>', driver_info, name='driver_info'),
    path('drivers/add-driver', add_driver, name='add_driver'),
    path('trucks/', trucks_list),
    path('trucks/<truck_id>', truck_info, name='truck_info'),
    path('trailors/', trailors_list),
    path('trailors/<trailor_id>', trailor_info, name='trailor_info'),
    path('loads/', loads_list),
    path('loads/<load_id>', load_info, name='load_info'),
]
