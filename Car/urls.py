from django.conf.urls import url
from Car import views

app_name = 'Car'

urlpatterns = [
        
    url(r'^$', views.cars, name='cars'),
    url(r'^car(?P<slug>[\w-]+)/$', views.car, name='car_detail'),
    ]