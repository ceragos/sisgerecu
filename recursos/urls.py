from django.contrib.auth.decorators import login_required
from django.urls import path

from recursos.views import RecursoFisicoListView, RecursoTecnologicoListView, RecursoFisicoCreateView, \
    RecursoTecnologicoCreateView, RecursoFisicoUpdateView, RecursoTecnologicoUpdateView, RecursoFisicoDeleteView, \
    RecursoTecnologicoDeleteView

urlpatterns = [
    # Recursos Fisicos
    path(r'fisicos/', login_required(RecursoFisicoListView.as_view()), name='recursos.fisicos.listar'),
    path(r'fisicos/crear', login_required(RecursoFisicoCreateView.as_view()), name='recursos.fisicos.crear'),
    path(r'fisicos/actualizar/<int:pk>', login_required(RecursoFisicoUpdateView.as_view()),
         name='recursos.fisicos.actualizar'),
    path(r'fisicos/eliminar/<int:pk>', login_required(RecursoFisicoDeleteView.as_view()),
         name='recursos.fisicos.eliminar'),

    # Recursos Tecnologicos
    path(r'tecnologicos/', login_required(RecursoTecnologicoListView.as_view()), name='recursos.tecnologicos.listar'),
    path(r'tecnologicos/crear', login_required(RecursoTecnologicoCreateView.as_view()),
         name='recursos.tecnologicos.crear'),
    path(r'tecnologicos/actualizar/<int:pk>', login_required(RecursoTecnologicoUpdateView.as_view()),
         name='recursos.tecnologicos.actualizar'),
    path(r'tecnologicos/eliminar/<int:pk>', login_required(RecursoTecnologicoDeleteView.as_view()),
         name='recursos.tecnologicos.eliminar'),
]
