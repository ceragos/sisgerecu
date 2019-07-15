from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView

from agendas.forms import AgendaForm
from agendas.models import Agenda


class AgendaListView(ListView):

    model = Agenda
    paginate_by = 100
    template_name = 'agendas/listar.html'
    context_object_name = 'agendas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AgendaCreateView(CreateView):

    model = Agenda
    form_class = AgendaForm
    template_name = 'agendas/crear.html'
    success_url = reverse_lazy('agendas.listar')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super(AgendaCreateView, self).form_valid(form)


class AgendaUpdateView(UpdateView):
    pass


class AgendaDeleteView(DeleteView):
    pass
