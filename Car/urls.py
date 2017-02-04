from django.conf.urls import url

from Car import views

app_name = 'Car'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^cars/$', views.car_list, name='car_list'),
    url(r'^car/(?P<id>\d+)/$', views.car_detail, name='car_detail'),
]