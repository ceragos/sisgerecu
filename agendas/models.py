from django.db import models
from nucleo.models import MarcadorTiempo
from recursos.models import RecursoFisico, RecursoTecnologico
from usuarios.models import User
from django.utils.timezone import now


ESTADO_RESERVA_CHOICES = (
    ('E', 'Entregado'),
    ('R', 'Recibido'),
)


def get_display(key, list):
    d = dict(list)
    if key in d:
        return d[key]
    return None


class Agenda(MarcadorTiempo):
    """ Almacena la agenda programada por los docentes. """
    usuario = models.ForeignKey(User, null=True, blank=True, verbose_name='User', on_delete=models.PROTECT,
                                related_name='usuario_agenda')
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
    """ Almacena la información que considera necesaria el personal de servicios generales. """
    reserva = models.OneToOneField(Agenda, null=False, blank=False, verbose_name='reserva en la agenda',
                                   related_name='reserva_agenda', on_delete=models.PROTECT)
    estado = models.CharField(max_length=1, blank=False, null=False, choices=ESTADO_RESERVA_CHOICES,
                              verbose_name='estado')
    observacion = models.TextField(null=True, blank=True, verbose_name='observacion')
    servicios_generales = models.ForeignKey(User, null=True, blank=True, verbose_name='servicios generales',
                                            on_delete=models.PROTECT)
    fecha_registro = models.DateField(null=False, blank=False, verbose_name='Fecha de Separación', default=now())

    def estado_verbose(self):
        return get_display(self.estado, ESTADO_RESERVA_CHOICES)

    def __str__(self):
        return '{}'.format(self.reserva)
