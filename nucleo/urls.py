from django.conf.urls import url
from django.urls import path

from nucleo.views import index

urlpatterns = [
    path(r'', index, name='index'),
]