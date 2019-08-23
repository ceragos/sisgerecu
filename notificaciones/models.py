from django.db import models

from nucleo.models import MarcadorTiempo
from usuarios.models import User


class ComunicacionInterna(MarcadorTiempo):
    remitente = models.ForeignKey(User, null=False, blank=False, verbose_name='remitente', on_delete=models.PROTECT,
                                  related_name='remitente_usuario')
    destinatario = models.ForeignKey(User, null=False, blank=False, verbose_name='destinatario',
                                     on_delete=models.PROTECT, related_name='destinatario_usuario')
    mensaje = models.TextField(null=False, blank=False, verbose_name='mensaje')
