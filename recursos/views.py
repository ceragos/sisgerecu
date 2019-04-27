from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from recursos.models import RecursoFisico, RecursoTecnologico


class RecursoFisicoListView(ListView):
    model = RecursoFisico
    paginate_by = 100  # if pagination is desired
    template_name = 'recursos/fisicos/listar.html'
    context_object_name = 'recursos_fisicos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class RecursoTecnologicoListView(ListView):
    model = RecursoTecnologico
    paginate_by = 100  # if pagination is desired
    template_name = 'recursos/tecnologicos/listar.html'
    context_object_name = 'recursos_tecnologicos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context