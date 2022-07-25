from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Truck
from drivers.models import Driver
from django.contrib.auth.decorators import login_required
from .forms import SearchTruckForm, AddTruckForm, DeleteTruckForm

# Create your views here.
@login_required
def trucks_list(request):
    form = SearchTruckForm()

    if request.method == "POST":
        form = SearchTruckForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']

            if search == "":
                trucks = Truck.objects.all()

            else:
                trucks = Truck.objects.filter(truck_number__contains=search)
    
    else:
        form = SearchTruckForm()
        trucks = Truck.objects.all()
    
    return render(request, 'trucks/trucks_list.html', {'trucks':trucks, 'form': form})

@login_required
def truck_info(request, truck_id):
    truck = Truck.objects.get(pk=truck_id)
    return render(request, 'trucks/truck_info.html', {'truck':truck})

@login_required
def add_truck(request):

    form = AddTruckForm()
    error=""

    if request.method == "POST":
        form = AddTruckForm(request.POST)

        if form.is_valid():
            truck_number = form.cleaned_data['truck_number']
            driver_assigned = form.cleaned_data['driver_assigned_to']

            if Truck.objects.filter(truck_number=truck_number).exists() != True and Driver.objects.filter(first_name=driver_assigned).exists():
                form.save()

            if Truck.objects.filter(truck_number=truck_number).exists() and Driver.objects.filter(first_name=driver_assigned).exists():
                form = AddTruckForm()
                error = "There is a driver with this truck number already, please try again."

            if Truck.objects.filter(truck_number=truck_number).exists() != True and Driver.objects.filter(first_name=driver_assigned).exists() != True:
                form = AddTruckForm()
                error = "There is no driver with this first name, please try again."


            else:
                form = AddTruckForm()
                error = "There is a user with this truck number already, please try again.\nThere is no driver with this first name, please try again."

    return render(request, 'trucks/add_truck.html', {'form': form, 'error': error})

def delete_truck(request):

    form = DeleteTruckForm()
    error = ''

    if request.method == "POST":
        form = DeleteTruckForm(request.POST)

        if form.is_valid():
            truck_number = form.cleaned_data['truck_number']

            if Truck.objects.filter(truck_number=truck_number).exists() == True:
                delete_truck = get_object_or_404(Truck, truck_number=truck_number)
                delete_truck.delete()
                return redirect('/')

            if Truck.objects.filter(truck_number=truck_number).exists() != True:
                form = DeleteTruckForm()
                error = "There is no truck that matches this truck number, please try again."
           
    return render(request, 'trucks/delete_truck.html', {'form': form, 'error': error})