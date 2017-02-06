from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse

from .models import Spec, Brand
from Car.forms import SpecForm


def index(request):
    list = Spec.objects.all()
    return render(request, "car/index.html", {'list': list})

    
def cars(request):
    cars = Spec.objects.filter(category='CAR')
    return render(request, "car/cars.html", {'cars': cars})


def car_detail(request, spec_id):
    try:
        car = Spec.objects.get(pk=spec_id)
    except Spec.DoesNotExist:
        raise Http404("Car doesnt exist")
    return render(request, "car/car_list.html", {'car': car})


def motorcycles(request):
    motorcycles = Spec.objects.filter(category='MOTORCYCLE')
    return render(request, "motorcycles/motorcycles.html", {'motorcycles': motorcycles})


def vehicles(request):
    vehicles = Spec.objects.filter(category='VEHICLE')
    return render(request, "vehicles/vehicles.html", {'vehicles': vehicles})


def car_detail(request, spec_id):
    try:
        car = Spec.objects.get(pk=spec_id)
    except Spec.DoesNotExist:
        raise Http404("Car doesnt exist")
    return render(request, "car/car_list.html", {'car': car})


def spec_form(request, id=None):
    if request.method == "POST":
        spec_form = SpecForm(request.POST)
        if spec_form.is_valid():
            spec = spec_form.save()
        return HttpResponseRedirect(reverse('car:all'))
    
    else:
        if id:
            spec =get_object_or_404(Spec, id=id)
            spec_form = SpecForm(instance=spec)
        
        else:
            spec_form = SpecForm()
    
    return render(request, "spec_form.html", {'spec_form': spec_form})