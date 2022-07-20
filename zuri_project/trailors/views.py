from django.shortcuts import render
from .models import Trailor
from django.contrib.auth.decorators import login_required
from .forms import SearchTrailorForm

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