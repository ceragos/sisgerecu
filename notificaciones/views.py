from dateutil.utils import today
from django.db.models import Q
from django.views.generic import ListView

from notificaciones.models import ComunicacionInterna


class ComunicacionInternaListView(ListView):
    model = ComunicacionInterna
    context_object_name = 'comunicacion'
    template_name = 'notificaciones/comunicaciones/listar.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hoy'] = today()
        return context

    def get_queryset(self):
        queryset = super(ComunicacionInternaListView, self).get_queryset()
        return queryset.filter(Q(destinatario=self.request.user) | Q(remitente=self.request.user))\
            .order_by('fecha_creacion')
