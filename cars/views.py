from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from cars.models import Car, CarInventory
from cars.forms import CarModelForm
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class NewCarView(View):
    
    def get(self, request):
        new_car_form = CarModelForm()
        
        return render(request, 'new_car.html', {'new_car_form': new_car_form})
    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        
        
class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('-brand')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)            
        return cars
        
        
@method_decorator(login_required(login_url='login'), name='dispatch')        
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'
       
@method_decorator(login_required(login_url='login'), name='dispatch')        
class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    
@method_decorator(login_required(login_url='login'), name='dispatch')        
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    
    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
    
@method_decorator(login_required(login_url='login'), name='dispatch')        
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = reverse_lazy('cars_list')  


@method_decorator(login_required(login_url='login'), name='dispatch')        
class CarInventoryListView(ListView):
    model = CarInventory
    template_name = 'cars_estoque.html'
    context_object_name = 'inventory'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        inventory = CarInventory.objects.first()
        if inventory:
            context['cars_count'] = inventory.cars_count
            context['cars_value'] = inventory.cars_value
            context['created_at'] = inventory.created_at
        return context
