# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from talento_humano.forms import EmpleadoForm
from talento_humano.models import Empleado

# Create your views here.
class EmpleadoListView(ListView):

    model = Empleado
    paginate_by = 100  # if pagination is desired
    template_name = 'talento_humano/listar.html'
    context_object_name = 'talento_humano'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'talento_humano/crear.html'
    success_url = reverse_lazy('empleado.list')


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'talento_humano/actualizar.html'
    success_url = reverse_lazy('empleado.list')


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'talento_humano/eliminar.html'
    success_url = reverse_lazy('empleado.list')