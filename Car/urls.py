from django.conf.urls import url

from Car import views

app_name = 'Car'

urlpatterns = [
	url(r'^$', views.index)

]