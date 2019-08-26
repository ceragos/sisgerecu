from dateutil.utils import today
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from agendas.models import Agenda
from notificaciones.forms import ComunicacionInternaForm
from notificaciones.models import ComunicacionInterna


class ComunicacionInternaListView(ListView):
    model = ComunicacionInterna
    context_object_name = 'comunicacion'
    template_name = 'notificaciones/comunicacion_interna/listar.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hoy'] = today()
        return context

    def get_queryset(self):
        queryset = super(ComunicacionInternaListView, self).get_queryset()
        f = self.request.GET['f']
        if f == 'inbox':
            queryset = queryset.filter(destinatario=self.request.user)
        elif f == 'send':
            queryset = queryset.filter(remitente=self.request.user)
        return queryset.order_by('-fecha_creacion')


class ComunicacionInternaCreateView(CreateView):
    model = ComunicacionInterna
    form_class = ComunicacionInternaForm
    template_name = 'notificaciones/comunicacion_interna/crear.html'
    context_object_name = 'comunicacion'
    success_url = reverse_lazy('agenda_general.listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reserva'] = Agenda.objects.get(id=self.kwargs['id_reserva'])
        return context

    def get_form_kwargs(self):
        kwargs = super(ComunicacionInternaCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        print('valido')
        return super(ComunicacionInternaCreateView, self).form_valid(form)

    def form_invalid(self, form):
        print('invalido')
        from django.http import HttpResponse
        return HttpResponse(form.cleaned_data)


class ComunicacionInternaDetailView(DetailView):
    model = ComunicacionInterna
    template_name = 'notificaciones/comunicacion_interna/detalle.html'
    context_object_name = 'mensaje'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mensaje = self.object
        if mensaje.destinatario == self.request.user:
            mensaje.estado = True
            mensaje.save()
        return context
