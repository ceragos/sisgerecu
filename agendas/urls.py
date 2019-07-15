from django.contrib.auth.decorators import login_required
from django.urls import path

from agendas.views import AgendaListView, AgendaCreateView

urlpatterns = [

    path(r'', login_required(AgendaListView.as_view()), name='agendas.listar'),
    path(r'crear/', login_required(AgendaCreateView.as_view()), name='agendas.crear'),
]
