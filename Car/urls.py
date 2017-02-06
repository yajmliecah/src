from django.conf.urls import url

from Car import views


app_name = 'Car'

urlpatterns = [
    url(r'^all/$', views.index),
    url(r'^cars/$', views.cars, name='cars'),
    url(r'^motorcycles/$', views.motorcycles, name='motorcycles'),
    url(r'^vehicles/$', views.vehicles, name='vehicles'),
    url(r'^car/(?P<id>\d+)/$', views.car_detail, name='car_detail'),
    url(r'^add/$', views.spec_form, name='spec_form'),
]