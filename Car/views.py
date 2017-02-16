from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template import Context, loader
from django.shortcuts import render, redirect, get_object_or_404

from .forms import SpecForm
from .models import Spec, Brand

from django.views.generic import ListView, DetailView, FormView

def index(request):
    list = Spec.objects.all()
    return render(request, 'car/index.html', {"list": list })


def cars(request):
    cars = Spec.objects.filter(category='CAR')
    return render(request, 'car/cars.html', {"cars": cars })


def motorcyles(request):
    motorcyles = Spec.objects.filter(category='MOTORCYCLES')
    return render(request, 'car/motorcycles.html', {"motorcycles": motorcyles })


def vehicles(request):
    vehicles = Spec.objects.filter(category='VEHICLES')
    return render(request, 'car/vehicles.html', {"vehicles": vehicles })


def car_detail(request, slug):
    car = get_object_or_404(Spec, slug=slug)
    return render(request, 'car/car_detail.html', {"car": car })


def motorcycle_detail(request, slug):
    motorcyle = get_object_or_404(Spec, slug=slug)
    return render(request, 'car/car_detail.html', {"motorcycle": motorcyle})


def vehicle_detail(request, slug):
    vehicle = get_object_or_404(Spec, slug=slug)
    return render(request, 'car/car_detail.html', {"vehicle": vehicle })