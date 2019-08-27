from datetime import datetime, date

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView

from agendas.forms import AgendaForm, FechaForm, MinutaForm
from agendas.models import Agenda, Minuta


class AgendaGeneralListView(ListView):

    model = Agenda
    paginate_by = 100
    template_name = 'agendas/agenda_general/agenda_general.html'
    context_object_name = 'agendas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FechaForm
        return context

    def get_queryset(self):
        queryset = super(AgendaGeneralListView, self).get_queryset()
        fecha = date.today()
        if self.request.GET.get('fecha'):
            from datetime import datetime
            fecha_str = self.request.GET.get('fecha')
            fecha = datetime.strptime(fecha_str, '%d-%m-%Y')
        return queryset.filter(fecha_separacion=fecha)


class MiAgendaListView(ListView):

    model = Agenda
    paginate_by = 100
    template_name = 'agendas/mi_agenda/listar.html'
    context_object_name = 'agendas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FechaForm
        return context

    def get_queryset(self):
        queryset = super(MiAgendaListView, self).get_queryset()
        fecha = date.today()
        if self.request.GET.get('fecha'):
            from datetime import datetime
            fecha_str = self.request.GET.get('fecha')
            fecha = datetime.strptime(fecha_str, '%d-%m-%Y')
        return queryset.filter(usuario=self.request.user).filter(fecha_separacion=fecha)


class MiAgendaCreateView(CreateView):

    model = Agenda
    form_class = AgendaForm
    template_name = 'agendas/mi_agenda/crear.html'

    def get_success_url(self):
        return reverse_lazy('mi_agenda.listar') + '?create_ok'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super(MiAgendaCreateView, self).form_valid(form)


class MiAgendaUpdateView(UpdateView):
    model = Agenda
    form_class = AgendaForm
    template_name = 'agendas/mi_agenda/actualizar.html'

    def get_success_url(self):
        return reverse_lazy('mi_agenda.listar') + '?edit_ok'


class MiAgendaDeleteView(DeleteView):
    model = Agenda
    template_name = 'agendas/mi_agenda/eliminar.html'
    success_url = reverse_lazy('mi_agenda.listar')


class MinutaListView(ListView):
    model = Minuta
    template_name = 'agendas/minuta/listar.html'
    paginate_by = 100
    context_object_name = 'minutas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FechaForm
        return context

    def get_queryset(self):
        queryset = super(MinutaListView, self).get_queryset()
        fecha = date.today()
        if self.request.GET.get('fecha'):
            from datetime import datetime
            fecha_str = self.request.GET.get('fecha')
            fecha = datetime.strptime(fecha_str, '%d-%m-%Y')
        return queryset.filter(fecha_registro=fecha)


class MinutaCreateView(CreateView):
    model = Minuta
    form_class = MinutaForm
    template_name = 'agendas/minuta/crear.html'
    context_object_name = 'minuta'
    success_url = reverse_lazy('minuta.listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reserva'] = Agenda.objects.get(id=self.kwargs['id_reserva'])
        data = {
            'reserva': Agenda.objects.get(id=self.kwargs['id_reserva']),
            'servicios_generales': self.request.user,
            'estado': 'E'
        }
        data_form = {
            'reserva': self.kwargs['id_reserva'],
            'servicios_generales': self.request.user.id,
            'estado': 'E'
        }
        form = MinutaForm(data_form)
        context['form'] = form
        context['data'] = data
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(MinutaCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(MinutaCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_invalid(self, form):
        from django.http import HttpResponse
        return HttpResponse(form.cleaned_data)
