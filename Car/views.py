from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .forms import SpecForm, SearchForm
from .models import Spec, Brand


def index(request):
    list = Spec.objects.all()
    return render(request, 'car/index.html', {"list": list })


def cars(request):
    cars = Spec.objects.filter(category='CAR')
    return render(request, 'car/cars.html', {"cars": cars })


def motorcyles(request):
    motorcyles = Spec.objects.filter(category='MOTORCYCLE')
    return render(request, 'car/motorcycles.html', {"motorcycles": motorcyles })


def vehicles(request):
    vehicles = Spec.objects.filter(category='VEHICLE')
    return render(request, 'car/vehicles.html', {"vehicles": vehicles })


def car_detail(request, slug):
    car = get_object_or_404(Spec, slug=slug)
    return render(request, 'car/car_detail.html', {"car": car })


def motorcycle_detail(request, slug):
    motorcyle = get_object_or_404(Spec, slug=slug)
    return render(request, 'car/motorcycle_detail.html', {"motorcycle": motorcyle})


def vehicle_detail(request, slug):
    vehicle = get_object_or_404(Spec, slug=slug)
    return render(request, 'car/vehicle_detail.html', {"vehicle": vehicle })


def search(request):
    query = request.GET.get('q')
    if query is not None and query != '' and request.is_ajax():
        list = Spec.objects.filter(Q(name__icontains=query))
        
        return render(request, 'car/search.html', {"list": list})
    
    return render(request, 'car/search.html')