from django.urls import path

from recursos.views import RecursoFisicoListView, RecursoTecnologicoListView, RecursoFisicoCreateView, \
    RecursoTecnologicoCreateView

urlpatterns = [
    # Recursos Fisicos
    path(r'fisicos/', RecursoFisicoListView.as_view(), name='recursos.fisicos.listar'),
    path(r'fisicos/crear', RecursoFisicoCreateView.as_view(), name='recursos.fisicos.crear'),

    # Recursos Tecnologicos
    path(r'tecnologicos/', RecursoTecnologicoListView.as_view(), name='recursos.tecnologicos.listar'),
    path(r'tecnologicos/crear', RecursoTecnologicoCreateView.as_view(), name='recursos.tecnologicos.crear')
]