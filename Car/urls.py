from django.conf.urls import url

from Car import views

app_name = 'Car'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^cars/(?P<list_id>[0-9]+)/$', views.car_detail, name='car_detail'),
]