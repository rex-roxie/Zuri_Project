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
from drivers.views import driver_info, drivers_list
from trucks.views import truck_info, trucks_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('', include('django.contrib.auth.urls')),
    path('drivers', drivers_list),
    path('driver/<driver_id>', driver_info, name='driver_info'),
    path('trucks', trucks_list),
    path('truck/<truck_id>', truck_info, name='truck_info'),
]
