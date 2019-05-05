from django.urls import path

from usuarios.views import SisgerecuLoginView

urlpatterns = [
    path(r'login/', SisgerecuLoginView.as_view(), name='login'),
]