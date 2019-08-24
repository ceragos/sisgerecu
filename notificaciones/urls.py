from django.contrib.auth.decorators import login_required
from django.urls import path

from notificaciones.views import ComunicacionInternaListView

urlpatterns = [
    path('comunicacion/listar/', login_required(ComunicacionInternaListView.as_view()), name='comunicacion.listar')
]
