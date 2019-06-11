from django.urls import path

from usuarios.views import SisgerecuLoginView, SisgerecuLogoutView, obtener_numero_celular

urlpatterns = [
    path(r'login/', SisgerecuLoginView.as_view(), name='login'),
    path(r'logout/', SisgerecuLogoutView.as_view(), name='logout'),
    path(r'obtener_numero_celular/<str:usuario>/', obtener_numero_celular, name='usuario.obtener_numero_celular')
]