from django.contrib.auth.decorators import login_required
from django.urls import path

from agendas.views import MiAgendaListView, AgendaGeneralListView, MiAgendaCreateView, MiAgendaUpdateView, \
    MiAgendaDeleteView, MinutaListView, MinutaCreateView

urlpatterns = [

    path(r'agenda_general/', login_required(AgendaGeneralListView.as_view()), name='agenda_general.listar'),

    path(r'mi_agenda/', login_required(MiAgendaListView.as_view()), name='mi_agenda.listar'),
    path(r'mi_agenda/crear/', login_required(MiAgendaCreateView.as_view()), name='agendas.crear'),
    path(r'mi_agenda/actualizar/<int:pk>', login_required(MiAgendaUpdateView.as_view()), name='agendas.actualizar'),
    path(r'mi_agenda/eliminar/<int:pk>', login_required(MiAgendaDeleteView.as_view()), name='agendas.eliminar'),

    path(r'minuta/', login_required(MinutaListView.as_view()), name='minuta.listar'),
    path(r'minuta/crear/<int:id_reserva>/', login_required(MinutaCreateView.as_view()), name='minuta.crear')
]
