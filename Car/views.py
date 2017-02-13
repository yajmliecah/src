from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template import Context, loader
from django.shortcuts import render, redirect, get_object_or_404

from .forms import SpecForm
from .models import Spec, Brand

from django.views.generic import ListView, DetailView, FormView


def cars(request):
    cars = Spec.objects.all()
    return render(request, 'car/cars.html', {"cars": cars })


def car(request, slug):
    car = get_object_or_404(Spec, slug=slug)
    return render(request, 'car/car_detail.html', {"car": car })