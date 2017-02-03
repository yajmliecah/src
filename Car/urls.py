from django.conf.urls import url

from Car import views

app_name = 'Car'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<list_id>\d+)/$', views.car_detail, name='car_detail'),
    url(r'^cars/(?P<list_id>\d+)/$', views.cars, name='cars'),
]