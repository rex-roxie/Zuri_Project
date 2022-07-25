from lib2to3.pgen2 import driver
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect

from drivers.models import Driver
from .models import Load
from django.contrib.auth.decorators import login_required
from .forms import SearchLoadForm, AddLoadForm, DeleteLoadForm

# Create your views here.
@login_required
def loads_list(request):
    form = SearchLoadForm()

    if request.method == "POST":
        form = SearchLoadForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']

            if search == "":
                loads = Load.objects.all()

            else:
                loads = Load.objects.filter(load_number__contains=search)
    
    else:
        form = SearchLoadForm()
        loads = Load.objects.all()
    
    return render(request, 'loads/loads_list.html', {'loads':loads, 'form': form})

@login_required
def load_info(request, load_id):
    load = load.objects.get(pk=load_id)
    return render(request, 'loads/load_info.html', {'load':load})

@login_required
def add_load(request):

    form = AddLoadForm()
    error=""

    if request.method == "POST":
        form = AddLoadForm(request.POST)

        if form.is_valid():
            load_number = form.cleaned_data['load_number']
            driver_assigned = form.cleaned_data['driver_assigned_to']

            if Load.objects.filter(load_number=load_number).exists() != True and Driver.objects.filter(first_name=driver_assigned).exists():
                new_load = Load.objects.create(new_load)
                new_load.save()
                print(new_load)

            if Load.objects.filter(load_number=load_number).exists() and Driver.objects.filter(first_name=driver_assigned).exists():
                form = AddLoadForm()
                error = "There is a driver with this load number already, please try again."

            if Load.objects.filter(load_number=load_number).exists() != True and Driver.objects.filter(first_name=driver_assigned).exists() != True:
                form = AddLoadForm()
                error = "There is no driver with this first name, please try again."


            else:
                form = AddLoadForm()
                error = "There is a user with this load number already, please try again.\nThere is no driver with this first name, please try again."

    return render(request, 'loads/add_load.html', {'form': form, 'error': error})

def delete_load(request):

    form = DeleteLoadForm()
    error = ''

    if request.method == "POST":
        form = DeleteLoadForm(request.POST)

        if form.is_valid():
            load_number = form.cleaned_data['load_number']

            if Load.objects.filter(load_number=load_number).exists() == True:
                delete_load = get_object_or_404(Load, load_number=load_number)
                delete_load.delete()
                return redirect('/')

            if Load.objects.filter(load_number=load_number).exists() != True:
                form = DeleteLoadForm()
                error = "There is no load that matches this load number, please try again."
           
    return render(request, 'loads/delete_load.html', {'form': form, 'error': error})