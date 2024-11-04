from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from urllib3 import request

from catalog.forms import BuildingForm
from catalog.models import Building


def index(request):
    buildings = Building.objects.all()
    paginator = Paginator(buildings,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj':page_obj})

def building(request, id):
    building = get_object_or_404(Building, id=id)
    return render(request, 'building.html', {'building':building})

def create_building(request):
    if request.method == 'POST':
        form = BuildingForm(request.POST, request.FILES)
        if form.is_valid:
            building = form.save(commit=False)
            building.user_id = request.user
            building.save()
            return redirect('index')
    else:
            form = BuildingForm()
    return render(request, 'creation.html', {'form':form})

def my_catalog(request, id):
    buildings = Building.objects.filter(user_id=id)
    return render(request, 'my_catalog.html', {'buildings':buildings})

def delete(request, id):
    if request.method == 'POST':
        building = get_object_or_404(Building, id=id)
        building.delete()
        return redirect('my_catalog', id=request.user.id)