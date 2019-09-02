from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path

from usuarios.views import SisgerecuLoginView, SisgerecuLogoutView, obtener_numero_celular

urlpatterns = [
    path(r'login/', SisgerecuLoginView.as_view(), name='login'),
    path(r'logout/', SisgerecuLogoutView.as_view(), name='logout'),
    path(r'obtener_numero_celular/<str:usuario>/', obtener_numero_celular, name='usuario.obtener_numero_celular'),

    path(r'password_change/', PasswordChangeView.as_view(template_name='usuarios/password_change_form.html'),
         name='password_change'),
    path(r'password_change_done/', PasswordChangeDoneView.as_view(template_name='usuarios/password_change_done.html'),
         name='password_change_done')
]
