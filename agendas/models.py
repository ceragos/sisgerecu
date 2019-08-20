from dateutil.utils import today
from django.db import models
from nucleo.models import MarcadorTiempo
from recursos.models import RecursoFisico, RecursoTecnologico
from usuarios.models import User


class Agenda(MarcadorTiempo):
    usuario = models.ForeignKey(User, null=True, blank=True, verbose_name='User', on_delete=models.PROTECT)
    recurso_fisico = models.ForeignKey(RecursoFisico, null=False, blank=False, verbose_name='recurso físico',
                                       on_delete=models.PROTECT)
    recurso_tecnologico = models.ManyToManyField(RecursoTecnologico, blank=True,
                                                 verbose_name='recurso tecnólogico', related_name='agenda_recurso')
    fecha_separacion = models.DateField(null=False, blank=False, verbose_name='Fecha de Separación', default=today())
    hora_separacion = models.TimeField(null=False, blank=False, verbose_name='Hora de Separación')
    hora_devolucion = models.TimeField(null=False, blank=False, verbose_name='Hora de Devolución')

    class Meta:
        verbose_name = 'agenda'
        verbose_name_plural = 'agendas'

    def __str__(self):
        return 'Separado por {} el {} desde las {} hasta las {}'.format(self.usuario.nombre_completo,
                                                                        self.fecha_separacion, self.hora_separacion,
                                                                        self.hora_devolucion)
