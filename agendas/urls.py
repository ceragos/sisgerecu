from django.contrib.auth.decorators import login_required
from django.urls import path

from agendas.views import MiAgendaListView, AgendaCreateView, AgendaGeneralListView

urlpatterns = [

    path(r'agenda_general', login_required(AgendaGeneralListView.as_view()), name='agenda_general.listar'),
    path(r'mi_agenda', login_required(MiAgendaListView.as_view()), name='mi_agenda.listar'),
    path(r'crear/', login_required(AgendaCreateView.as_view()), name='agendas.crear'),
]
