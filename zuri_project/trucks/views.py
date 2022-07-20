from django.shortcuts import render
from .models import Truck
from django.contrib.auth.decorators import login_required
from .forms import SearchTruckForm

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