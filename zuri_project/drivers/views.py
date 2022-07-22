from django.shortcuts import render, get_object_or_404, redirect
from .models import Driver
from django.contrib.auth.decorators import login_required
from .forms import SearchDriverForm, AddDriverForm, DeleteDriverForm

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

@login_required
def add_driver(request):

    form = AddDriverForm()

    if request.method == "POST":
        form = AddDriverForm(request.POST)

        if form.is_valid():
            new_driver = form.save()
            new_driver = Driver.objects.create(new_driver)
            new_driver.save()
           
    return render(request, 'drivers/add_driver.html', {'form': form})

def delete_driver(request):

    form = DeleteDriverForm()

    if request.method == "POST":
        form = DeleteDriverForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            new_driver = get_object_or_404(Driver, first_name=first_name)
            new_driver.delete()
            return redirect('/')
           
    return render(request, 'drivers/delete_driver.html', {'form': form})

@login_required
def deleted_driver_successfully(request):
    return render(request, 'drivers/delete_driver_success.html', {})