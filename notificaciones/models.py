from django.db import models

from agendas.models import Agenda
from nucleo.models import MarcadorTiempo
from usuarios.models import User


class ComunicacionInterna(MarcadorTiempo):
    reserva = models.ForeignKey(Agenda, null=False, blank=False, verbose_name='reserva', on_delete=models.PROTECT)
    remitente = models.ForeignKey(User, null=False, blank=False, verbose_name='remitente', on_delete=models.PROTECT,
                                  related_name='remitente_usuario')
    destinatario = models.ForeignKey(User, null=False, blank=False, verbose_name='destinatario',
                                     on_delete=models.PROTECT, related_name='destinatario_usuario')
    mensaje = models.TextField(null=False, blank=False, verbose_name='mensaje')
    estado = models.BooleanField(default=False, verbose_name='mensaje leido')

    class Meta:
        verbose_name = 'comunicación interna'
        verbose_name_plural = 'comunicacion_interna internas'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return 'remite: {} / destino: {}'.format(self.remitente.username, self.destinatario.username)
