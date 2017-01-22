from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse

from Car.models import Spec, Condition, Brand
from Car.forms import forms


def index(request):
	return render(request, "index.html", {})


def car_list(request):
	cars = models.Specobjects.all()
	return render(request, "car_list.html", {'cars': cars})


def car_detail(request, id):
	id = int(id)
	cars = get_object_or_404(models.Spec, id=id)
	return render(request, "car_detail.html", {'cars': cars})
