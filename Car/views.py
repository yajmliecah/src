from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template import Context, loader
from django.shortcuts import render, redirect, render_to_response

from .forms import SpecForm
from .models import Spec


def index(request):
    list = Spec.objects.all()
    return render(request, "car/index.html", {'list': list})

    
def cars(request):
    cars = Spec.objects.filter(category='CAR')
    return render(request, "car/cars.html", {'cars': cars})


def car_detail(request, spec_id):
    try:
        cars = Spec.objects.get(pk=spec_id)
    except Spec.DoesNotExist:
        raise Http404
    
    return render_to_response('car/car_detail.html', {'cars': cars} )


def motorcycles(request):
    motorcycles = Spec.objects.filter(category='MOTORCYCLE')
    return render(request, "motorcycles/motorcycles.html", {'motorcycles': motorcycles})


def vehicles(request):
    vehicles = Spec.objects.filter(category='VEHICLE')
    return render(request, "vehicles/vehicles.html", {'vehicles': vehicles})


def spec_form(request, pk):
    if request.method == 'POST':
        form = SpecForm(request.POST)
        
        if form.is_valid():
            spec = form.save(commit=False)
            spec.save()
            return redirect('car_detail', pk=spec.pk)
        
    else:
        form = SpecForm()
    
    return render(request, 'spec_form.html', {'form': form})