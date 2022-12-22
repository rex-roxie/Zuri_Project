from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from drivers.models import Driver
from trucks.models import Truck
from trailors.models import Trailor
from loads.models import Load

# Create your views here.

def index(request):
    return render(request, 'authentication/index.html', {})

@login_required
def dashboard(request):

    driver_count= Driver.objects.all().count()
    truck_count= Truck.objects.all().count()
    trailor_count= Trailor.objects.all().count()
    load_count= Load.objects.all().count()
    driver_list = Driver.objects.all()
    truck_list = Driver.objects.all()
    trailor_list = Driver.objects.all()
    load_list = Driver.objects.all()

    context = {
        'driver_count': driver_count,
        'truck_count': truck_count,
        'trailor_count': trailor_count,
        'load_count': load_count,
        'driver_list': driver_list,
        'truck_list': truck_list,
        'trailor_list': trailor_list,
        'load_list': load_list,
    }
    return render(request, 'authentication/dashboard.html', context)