from django.urls import path

from talento_humano.views import EmpleadoListView, EmpleadoCreateView, EmpleadoUpdateView, EmpleadoDeleteView

urlpatterns = [
    path(r'', EmpleadoListView.as_view(), name='empleado.list'),
    path(r'crear_empleado/', EmpleadoCreateView.as_view(), name='empleado.create'),
    path(r'actualizar_empleado/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado.update'),
    path(r'eliminar_empleado/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado.delete'),
]