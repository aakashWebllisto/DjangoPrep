from django.shortcuts import render

# Create your views here.

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Car

class CarBaseView(View):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('Cars:all')

class CarListView(CarBaseView, ListView):
    """View to list all Cars.
    Use the 'Car_list' variable in the template
    to access all Car objects"""

class CarDetailView(CarBaseView, DetailView):
    """View to list the details from one Car.
    Use the 'Car' variable in the template to access
    the specific Car here and in the Views below"""

class CarCreateView(CarBaseView, CreateView):
    """View to create a new Car"""

class CarUpdateView(CarBaseView, UpdateView):
    """View to update a Car"""

class CarDeleteView(CarBaseView, DeleteView):
    """View to delete a Car"""
