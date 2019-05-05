from django.contrib.auth.decorators import login_required
from django.urls import path

from talento_humano.views import EmpleadoListView, EmpleadoCreateView, EmpleadoUpdateView, EmpleadoDeleteView

urlpatterns = [
    path(r'', login_required(EmpleadoListView.as_view()), name='empleado.list'),
    path(r'crear_empleado/', login_required(EmpleadoCreateView.as_view()), name='empleado.create'),
    path(r'actualizar_empleado/<int:pk>/', login_required(EmpleadoUpdateView.as_view()), name='empleado.update'),
    path(r'eliminar_empleado/<int:pk>/', login_required(EmpleadoDeleteView.as_view()), name='empleado.delete'),
]