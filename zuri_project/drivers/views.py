from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Driver
from django.contrib.auth.decorators import login_required
from .forms import SearchDriverForm, AddDriverForm, DeleteDriverForm
from django import forms

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
    error=""

    if request.method == "POST":
        form = AddDriverForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']

            if Driver.objects.filter(email=email).exists() != True:
                form.save()
                return redirect("/drivers/")
            
            else:
                form = AddDriverForm()
                error = "There is a user with this email already, please try again."

    return render(request, 'drivers/add_driver.html', {'form': form, 'error': error})

def delete_driver(request):

    form = DeleteDriverForm()

    if request.method == "POST":
        form = DeleteDriverForm(request.POST)

        if form.is_valid():
            phone = form.cleaned_data['phone']

            if Driver.objects.filter(phone=phone).exists() == True:
                new_driver = get_object_or_404(Driver, phone=phone)
                new_driver.delete()
                return redirect('/drivers/')

            else:
                form = DeleteDriverForm()
                error = "There is no driver that matches this phone number, please try again."
           
    return render(request, 'drivers/delete_driver.html', {'form': form})