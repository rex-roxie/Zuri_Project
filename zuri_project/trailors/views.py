from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Trailor
from drivers.models import Driver
from django.contrib.auth.decorators import login_required
from .forms import SearchTrailorForm, AddTrailorForm, DeleteTrailorForm

# Create your views here.
@login_required
def trailors_list(request):
    form = SearchTrailorForm()

    if request.method == "POST":
        form = SearchTrailorForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']

            if search == "":
                trailors = Trailor.objects.all()

            else:
                trailors = Trailor.objects.filter(trailor_number__contains=search)
    
    else:
        form = SearchTrailorForm()
        trailors = Trailor.objects.all()
    
    return render(request, 'trailors/trailors_list.html', {'trailors':trailors, 'form': form})

@login_required
def trailor_info(request, trailor_id):
    trailor = Trailor.objects.get(pk=trailor_id)
    return render(request, 'trailors/trailor_info.html', {'trailor':trailor})

@login_required
def add_trailor(request):

    form = AddTrailorForm()
    error=""

    if request.method == "POST":
        form = AddTrailorForm(request.POST)

        if form.is_valid():
            trailor_number = form.cleaned_data['trailor_number']
            driver_assigned = form.cleaned_data['driver_assigned_to']

            if Trailor.objects.filter(trailor_number=trailor_number).exists() != True and Driver.objects.filter(first_name=driver_assigned).exists():
                form.save()
                return redirect('/trailors/')

            if Trailor.objects.filter(trailor_number=trailor_number).exists() and Driver.objects.filter(first_name=driver_assigned).exists():
                form = AddTrailorForm()
                error = "There is a driver with this trailor number already, please try again."

            if Trailor.objects.filter(trailor_number=trailor_number).exists() != True and Driver.objects.filter(first_name=driver_assigned).exists() != True:
                form = AddTrailorForm()
                error = "There is no driver with this first name, please try again."


            else:
                form = AddTrailorForm()
                error = "There is a user with this trailor number already, please try again.\nThere is no driver with this first name, please try again."

    return render(request, 'trailors/add_trailor.html', {'form': form, 'error': error})

def delete_trailor(request):

    form = DeleteTrailorForm()
    error = ''

    if request.method == "POST":
        form = DeleteTrailorForm(request.POST)

        if form.is_valid():
            trailor_number = form.cleaned_data['trailor_number']

            if Trailor.objects.filter(trailor_number=trailor_number).exists() == True:
                delete_trailor = get_object_or_404(Trailor, trailor_number=trailor_number)
                delete_trailor.delete()
                return redirect('/trailors/')

            if Trailor.objects.filter(trailor_number=trailor_number).exists() != True:
                form = DeleteTrailorForm()
                error = "There is no trailor that matches this trailor number, please try again."
           
    return render(request, 'trailors/delete_trailor.html', {'form': form, 'error': error})