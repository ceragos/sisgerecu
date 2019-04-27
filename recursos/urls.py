from django.urls import path

from recursos.views import RecursoFisicoListView, RecursoTecnologicoListView, RecursoFisicoCreateView, \
    RecursoTecnologicoCreateView, RecursoFisicoUpdateView, RecursoTecnologicoUpdateView, RecursoFisicoDeleteView, \
    RecursoTecnologicoDeleteView

urlpatterns = [
    # Recursos Fisicos
    path(r'fisicos/', RecursoFisicoListView.as_view(), name='recursos.fisicos.listar'),
    path(r'fisicos/crear', RecursoFisicoCreateView.as_view(), name='recursos.fisicos.crear'),
    path(r'fisicos/actualizar/<int:pk>', RecursoFisicoUpdateView.as_view(), name='recursos.fisicos.actualizar'),
    path(r'fisicos/eliminar/<int:pk>', RecursoFisicoDeleteView.as_view(), name='recursos.fisicos.eliminar'),

    # Recursos Tecnologicos
    path(r'tecnologicos/', RecursoTecnologicoListView.as_view(), name='recursos.tecnologicos.listar'),
    path(r'tecnologicos/crear', RecursoTecnologicoCreateView.as_view(), name='recursos.tecnologicos.crear'),
    path(r'tecnologicos/actualizar/<int:pk>', RecursoTecnologicoUpdateView.as_view(), name='recursos.tecnologicos.actualizar'),
    path(r'tecnologicos/eliminar/<int:pk>', RecursoTecnologicoDeleteView.as_view(), name='recursos.tecnologicos.eliminar'),
]