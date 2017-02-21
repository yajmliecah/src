from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse

from .forms import SpecForm, SearchForm
from .models import Spec, Brand


def index(request):
    list = Spec.objects.all()
    return render(request, 'car/index.html', {"list": list })


def list_details(request, slug):
    list = get_object_or_404(Spec, slug=slug)
    return render(request, 'car/list_detail.html', {"list": list })


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
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        spec = Spec.objects.filter(name__icontains=q)
        return render(request, 'results.html',
                      {'spec': spec, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')


def add_form(request):
    
    if request.method == 'POST':
        form = SpecForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            
            return HttpResponseRedirect('/')
        
    
    else:
        form = SpecForm()
    
    return render(request, 'car/add_form.html', {"form": form})


def edit_form(request, pk):
    list = get_object_or_404(Spec, pk)
    if request.POST:
        form = SpecForm(request.POST, instance=list)
    
        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
    else:
        form = SpecForm()
    
    return render(request, 'car/edit_form.html', {"form": form })
            
        
def delete(request, pk):
    list = get_object_or_404(Spec, pk=pk)
    
    if request.method == 'POST':
        list.delete()
        
        return HttpResponseRedirect('/')
    
    return render(request, 'car/delete.html', {"list": list})
    
            
    
    
            
            
            
            
        