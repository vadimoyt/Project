from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from catalog.forms import BuildingForm
from catalog.models import Building
from user.models import CustomUser


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
    if request.user.is_authenticated and request.user.role == 'owner':
        if request.method == 'POST':
            form = BuildingForm(request.POST, request.FILES)
            if form.is_valid():
                building = form.save(commit=False)
                building.user_id = request.user
                building.save()
                return redirect('index')
        else:
                form = BuildingForm()
        return render(request, 'creation.html', {'form':form})
    return render(request, '403.html')

def my_catalog(request, id):
    if request.user.is_authenticated and request.user.role == 'owner':
        user = get_object_or_404(CustomUser, id=id)
        buildings = Building.objects.filter(user_id=user)
        return render(request, 'my_catalog.html', {'buildings':buildings})
    return render(request, '403.html')

def delete(request, id):
    if request.user.is_authenticated and request.user.role == 'owner':
        building = get_object_or_404(Building, id=id, user_id=request.user)
        if request.method == 'POST':
            building.delete()
            return redirect('my_catalog', id=request.user.id)
    return render(request, '403.html')


def change_data(request, id):
    if request.user.is_authenticated and request.user.role == 'owner':
        building = get_object_or_404(Building, id=id, user_id=request.user)
        if request.method == 'POST':
            form = BuildingForm(request.POST, request.FILES, instance=building)
            if form.is_valid():
                form.save()
                return redirect('my_catalog', id=request.user.id)
        else:
            form = BuildingForm(instance=building)
        return render(request, 'change_data.html', {'form': form, 'building': building})
    return render(request, '403.html')

def sorted_building(request):
    type_of_building = request.GET.get('category')
    square = request.GET.get('square')
    year = request.GET.get('year')
    buildings = Building.objects.all()
    if not type_of_building and not square:
        return redirect('index')
    if type_of_building:
        buildings = buildings.filter(type_of_building=type_of_building)
    if square:
        min_square, max_square = map(int, square.split('-'))
        buildings = buildings.filter(square__gte=min_square, square__lte=max_square)
    if year:
        min_year, max_year = map(int, year.split('-'))
        buildings = buildings.filter(year_of_construction__gte=min_year, year_of_construction__lte=max_year)
    paginator = Paginator(buildings, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'sorted_building.html', {'page_obj': page_obj})


