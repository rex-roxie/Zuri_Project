from django.shortcuts import render
from .models import Load
from django.contrib.auth.decorators import login_required
from .forms import SearchLoadForm

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