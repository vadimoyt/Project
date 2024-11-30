from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from catalog.forms import BuildingForm
from catalog.models import Building


class BuildingList(ListView):
    model = Building
    paginate_by = 4
    template_name = 'index.html'
    context_object_name = 'page_obj'


class BuildingDetail(DetailView):
    model = Building
    template_name = 'building.html'


class CreateBuilding(LoginRequiredMixin, CreateView):
    model = Building
    template_name = 'creation.html'
    form_class = BuildingForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.role == 'owner':
            return HttpResponseForbidden('You have no permissions')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response({'form':form})

    def get_success_url(self):
        return reverse_lazy('building', kwargs={'pk': self.object.pk})


class ListOfMyBuilding(ListView):
    model = Building
    template_name = 'my_catalog.html'
    paginate_by = 2
    context_object_name = 'user_buildings'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.role == 'owner':
            return HttpResponseForbidden('You have no permissions')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        return Building.objects.filter(user_id=user)


class DeleteMyObject(DeleteView):
    model = Building
    template_name = 'my_catalog.html'
    context_object_name = 'building'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or self.request.user.role != 'owner':
            return HttpResponseForbidden('You have no permissions')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('my_catalog', kwargs={'pk':self.request.user.id})

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user_id != self.request.user:
            raise PermissionDenied('No permission')
        return obj


class UpdateMyBuilding(UpdateView):
    model = Building
    form_class = BuildingForm
    template_name = 'change_data.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.role == 'owner':
            return HttpResponseForbidden('You have no permissions')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('my_catalog', kwargs={'pk':self.request.user.id})

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user_id != self.request.user:
            raise PermissionDenied('No permission')
        return obj


def sorted_building(request):
    type_of_building = request.GET.get('category')
    square = request.GET.get('square')
    year = request.GET.get('year')
    buildings = Building.objects.all()
    if not type_of_building and not square and not year:
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


