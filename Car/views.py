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


def car_detail(request, list_id):
    
    try:
        list = Spec.objects.get(pk=list_id)
    except Spec.DoesNotExist:
        raise Http404("Car does not exist")
    return render(request, 'car/car_detail.html', {'list': list})


def cars(request, car_list):
    car = Spec.objects.get()
    