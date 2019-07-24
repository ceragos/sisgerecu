from django.db import models
from nucleo.models import MarcadorTiempo
from recursos.models import RecursoFisico, RecursoTecnologico
from usuarios.models import User


class Agenda(MarcadorTiempo):
    usuario = models.ForeignKey(User, null=True, blank=True, verbose_name='User', on_delete=models.PROTECT)
    recurso_fisico = models.ForeignKey(RecursoFisico, null=False, blank=False, verbose_name='Recurso fisico',
                                       on_delete=models.PROTECT)
    recurso_tecnologico = models.ManyToManyField(RecursoTecnologico, blank=True,
                                                 verbose_name='Recurso Tecnologico', related_name='agenda_recurso',
                                                 help_text='Mantenga presionado "Control" o "Command" en un Mac, para '
                                                           'seleccionar más de una opción.')
    fecha_separacion = models.DateField(null=False, blank=False, verbose_name='Fecha de Separación')
    hora_separacion = models.TimeField(null=False, blank=False, verbose_name='Hora de Separación')
    hora_devolucion = models.TimeField(null=False, blank=False, verbose_name='Hora de Devolución')

    class Meta:
        verbose_name = 'agenda'
        verbose_name_plural = 'agendas'

    def __str__(self):
        return self.usuario.nombre_completo
