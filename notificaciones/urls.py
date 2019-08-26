from django.contrib.auth.decorators import login_required
from django.urls import path

from notificaciones.views import ComunicacionInternaListView, ComunicacionInternaCreateView, \
    ComunicacionInternaDetailView

urlpatterns = [
    path('comunicacion/listar/', login_required(ComunicacionInternaListView.as_view()), name='comunicacion.listar'),
    path('comunicacion/crear/<int:id_reserva>/', login_required(ComunicacionInternaCreateView.as_view()),
         name='comunicacion.crear'),
    path('comunicacion/detalle/<int:pk>/', login_required(ComunicacionInternaDetailView.as_view()),
         name='comunicacion.detalle')
]
