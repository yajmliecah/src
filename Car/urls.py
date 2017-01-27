from django.conf.urls import url

from Car import views

app_name = 'Car'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^$car/', views.car_list, name='car_list'),

]