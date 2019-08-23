from dateutil.utils import today
from django.db import models
from nucleo.models import MarcadorTiempo
from recursos.models import RecursoFisico, RecursoTecnologico
from usuarios.models import User
from django.utils.timezone import now


ESTADO_RESERVA_CHOICES = (
    ('P', 'Pendiente'),
    ('E', 'Entregado'),
    ('R', 'Recibido'),
)


class Agenda(MarcadorTiempo):
    usuario = models.ForeignKey(User, null=True, blank=True, verbose_name='User', on_delete=models.PROTECT)
    recurso_fisico = models.ForeignKey(RecursoFisico, null=False, blank=False, verbose_name='recurso físico',
                                       on_delete=models.PROTECT)
    recurso_tecnologico = models.ManyToManyField(RecursoTecnologico, blank=True,
                                                 verbose_name='recurso tecnólogico', related_name='agenda_recurso')
    fecha_separacion = models.DateField(null=False, blank=False, verbose_name='Fecha de Separación', default=now())
    hora_separacion = models.TimeField(null=False, blank=False, verbose_name='Hora de Separación')
    hora_devolucion = models.TimeField(null=False, blank=False, verbose_name='Hora de Devolución')

    class Meta:
        verbose_name = 'agenda'
        verbose_name_plural = 'agendas'

    def __str__(self):
        return 'Separado por {} el {} desde las {} hasta las {}'.format(self.usuario.nombre_completo,
                                                                        self.fecha_separacion, self.hora_separacion,
                                                                        self.hora_devolucion)


class Minuta(MarcadorTiempo):
    reserva = models.ForeignKey(Agenda, null=False, blank=False, verbose_name='reserva en la agenda',
                                related_name='reserva_agenda', on_delete=models.PROTECT)
    estado = models.CharField(max_length=1, blank=False, null=False, choices=ESTADO_RESERVA_CHOICES,
                              verbose_name='estado', default='P')
    observacion = models.TextField(null=True, blank=True, verbose_name='observacion')
    encargado = models.ForeignKey(User, null=False, blank=False, verbose_name='encargado', on_delete=models.PROTECT)
