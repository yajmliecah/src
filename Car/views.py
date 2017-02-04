from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from .models import Spec


def index(request):
    list = Spec.objects.all()
    return render(request, "car/index.html", {'list': list})

    
def car_list(request):
    cars = Spec.objects.all()
    return render(request, "car/car_list.html", {'cars': cars})


def car_detail(request, spec_id):
    try:
        car = Spec.objects.get(pk=spec_id)
    except Spec.DoesNotExist:
        raise Http404("Car doesnt exist")
    return render(request, "car/car_detail.html", {'car': car})


def cars(request, car_list):
    car = Spec.objects.filter(category='CAR')
    return render(request, "car/cars.html", {'car': car})


def motorcycles(request, motor_list):
    motor_list = Spec.objects.filter(category='MOTORCYCLES')
    return render(request, "car/motorcycles.html", {'motorcycles': motorcycles})