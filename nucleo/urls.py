from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path

from nucleo.views import index

urlpatterns = [
    path(r'', login_required(index), name='index'),
]