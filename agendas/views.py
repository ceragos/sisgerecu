from datetime import datetime, date

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView

from agendas.forms import AgendaForm, FechaForm
from agendas.models import Agenda


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
    success_url = reverse_lazy('mi_agenda.listar')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super(MiAgendaCreateView, self).form_valid(form)


class MiAgendaUpdateView(UpdateView):
    model = Agenda
    form_class = AgendaForm
    template_name = 'agendas/mi_agenda/actualizar.html'
    success_url = reverse_lazy('mi_agenda.listar')


class MiAgendaDeleteView(DeleteView):
    model = Agenda
    template_name = 'agendas/mi_agenda/eliminar.html'
    success_url = reverse_lazy('mi_agenda.listar')
