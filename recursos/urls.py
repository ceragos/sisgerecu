from django.urls import path

from recursos.views import RecursoFisicoListView, RecursoTecnologicoListView

urlpatterns = [
    # Recursos Fisicos
    path(r'fisicos/', RecursoFisicoListView.as_view(), name='recursos.fisicos.listar'),

    # Recursos Tecnologicos
    path(r'tecnologicos/', RecursoTecnologicoListView.as_view(), name='recursos.tecnologicos.listar'),
]