# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from talento_humano.forms import EmpleadoForm
from talento_humano.models import Empleado

# Create your views here.
from usuarios.forms import CrearUsuarioForm, ActualizarUsuarioForm
from usuarios.models import User


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
    form_class_user = CrearUsuarioForm
    template_name = 'talento_humano/crear.html'
    success_url = reverse_lazy('empleado.list')

    def get_context_data(self, **kwargs):
        context = super(EmpleadoCreateView, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form_user' not in context:
            context['form_user'] = self.form_class_user(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form_user = self.form_class_user(request.POST)
        if form.is_valid() and form_user.is_valid():
            empleado = form.save(commit=False)
            empleado.usuario = form_user.save()
            empleado.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form_user=form_user))


class EmpleadoUpdateView(UpdateView):

    model = Empleado
    model_user = User
    form_class = EmpleadoForm
    form_class_user = ActualizarUsuarioForm
    template_name = 'talento_humano/actualizar.html'
    success_url = reverse_lazy('empleado.list')

    def get_context_data(self, **kwargs):
        context = super(EmpleadoUpdateView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        empleado = self.model.objects.get(id=pk)
        usuario = self.model_user.objects.get(id=empleado.usuario_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form_user' not in context:
            context['form_user'] = self.form_class_user(instance=usuario)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_empleado = kwargs['pk']
        empleado = self.model.objects.get(id=id_empleado)
        usuario = self.model_user.objects.get(id=empleado.usuario_id)
        form = self.form_class(request.POST, instance=empleado)
        form_user = self.form_class_user(request.POST, instance=usuario)
        if form.is_valid() and form_user.is_valid():
            # empleado = form.save(commit=False)
            # empleado.usuario = form_user.save()
            form_user.save()
            empleado.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form_user=form_user))


class EmpleadoDeleteView(DeleteView):

    model = Empleado
    template_name = 'talento_humano/eliminar.html'
    success_url = reverse_lazy('empleado.list')
