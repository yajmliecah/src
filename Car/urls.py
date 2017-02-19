from django.conf.urls import url
from Car import views

app_name = 'Car'

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_form, name='add_form'),
    url(r'^cars/$', views.cars, name='cars'),
    url(r'^motorcycles/$', views.motorcyles, name='motorcycles'),
    url(r'^vehicles/$', views.vehicles, name='vehicles'),
    url(r'^(?P<slug>[-\w]+)/$', views.list_details, name='list'),
    url(r'^car/(?P<slug>[-\w]+)/$', views.car_detail, name='cars'),
    url(r'^motorcycle/(?P<slug>[-\w]+)/$', views.motorcycle_detail, name='motorcycles'),
    url(r'^vehicle/(?P<slug>[-\w]+)/$', views.vehicle_detail, name='vehicles'),
    url(r'^search/$', views.search, name='search'),
    ]