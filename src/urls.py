from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^', include('Car.urls', namespace='Car')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)