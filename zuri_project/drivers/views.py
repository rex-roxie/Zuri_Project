from lib2to3.pgen2.driver import Driver
from django.shortcuts import render
from .models import Driver
from django.contrib.auth.decorators import login_required
from .forms import SearchDriverForm

# Create your views here.
@login_required
def drivers_list(request):
    form = SearchDriverForm()

    if request.method == "POST":
        form = SearchDriverForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']

            if search == "":
                drivers = Driver.objects.all()

            else:
                drivers = Driver.objects.filter(first_name__contains=search)
    
    else:
        form = SearchDriverForm()
        drivers = Driver.objects.all()
    
    return render(request, 'drivers/drivers_list.html', {'drivers':drivers, 'form': form})

@login_required
def driver_info(request, driver_id):
    driver = Driver.objects.get(pk=driver_id)
    return render(request, 'drivers/driver_info.html', {'driver':driver})