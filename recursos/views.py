from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from recursos.forms import RecursoFisicoForm, RecursoTecnologicoForm
from recursos.models import RecursoFisico, RecursoTecnologico


class RecursoFisicoListView(ListView):
    model = RecursoFisico
    paginate_by = 100  # if pagination is desired
    template_name = 'recursos/fisicos/listar.html'
    context_object_name = 'recursos_fisicos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RecursoFisicoCreateView(CreateView):
    model = RecursoFisico
    form_class = RecursoFisicoForm
    template_name = 'recursos/fisicos/crear.html'
    success_url = reverse_lazy('recursos.fisicos.listar')


class RecursoTecnologicoListView(ListView):
    model = RecursoTecnologico
    paginate_by = 100  # if pagination is desired
    template_name = 'recursos/tecnologicos/listar.html'
    context_object_name = 'recursos_tecnologicos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RecursoTecnologicoCreateView(CreateView):
    model = RecursoTecnologico
    form_class = RecursoTecnologicoForm
    template_name = 'recursos/tecnologicos/crear.html'
    success_url = reverse_lazy('recursos.tecnologicos.listar')