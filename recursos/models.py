from django.db import models

# Create your models here.
from nucleo.models import MarcadorTiempo


class TipoEquipo(MarcadorTiempo):
    nombre = models.CharField(max_length=30, null=True, blank=True, verbose_name='nombre')

    class Meta:
        verbose_name = 'tipo de equipo'
        verbose_name_plural = 'tipos de equipo'
        ordering = ['nombre']

    def __str__(self):
        return '%s' % self.nombre


class TipoAula(MarcadorTiempo):
    nombre = models.CharField(max_length=30, null=True, blank=True, verbose_name='nombre')

    class Meta:
        verbose_name = 'tipo de aula'
        verbose_name_plural = 'tipos de aula'
        ordering = ['nombre']

    def __str__(self):
        return '%s' % self.nombre


class Recurso(models.Model):
    numero = models.IntegerField(verbose_name='numero', null=True, blank=True)
    contenido = models.TextField(verbose_name='contenido', null=True, blank=True)
    caracteristicas = models.TextField(verbose_name='caracteristicas', null=True, blank=True)

    class Meta:
        verbose_name = 'recurso'
        verbose_name_plural = 'recursos'


class RecursoFisico(MarcadorTiempo, Recurso):
    tipo_aula = models.ForeignKey(TipoAula, null=True, blank=True, verbose_name='tipo de aula',on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40, null=True, blank=True, verbose_name='nombre', unique=True)
    capacidad = models.IntegerField(verbose_name='capacidad', null=True, blank=True)
    ubicacion = models.CharField(max_length=40, null=True, blank=True, verbose_name='ubicación')

    class Meta:
        verbose_name = 'recurso fisico'
        verbose_name_plural = 'recursos fisicos'
        ordering = ['nombre']

    def __str__(self):
        return '%s' % self.nombre

    def save(self, *args, **kwargs):
        if not self.nombre:
            self.nombre = '%s %s' % (self.tipo_aula, self.numero)

        return super(RecursoFisico, self).save(*args, **kwargs)


class RecursoTecnologico(MarcadorTiempo, Recurso):
    tipo_equipo = models.ForeignKey(TipoEquipo, null=True, blank=True, verbose_name='tipo de equipo', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40, null=True, blank=True, verbose_name='nombre', unique=True)
    marca = models.CharField(max_length=40, null=True, blank=True, verbose_name='marca')
    referencia = models.CharField(max_length=40, null=True, blank=True, verbose_name='referencia')
    color = models.CharField(max_length=40, null=True, blank=True, verbose_name='color')

    class Meta:
        verbose_name = 'recurso tecnologico'
        verbose_name_plural = 'recursos tecnologicos'
        ordering = ['nombre']

    def __str__(self):
        return '%s' % self.nombre

    def save(self, *args, **kwargs):
        if not self.nombre:
            self.nombre = '%s %s' % (self.tipo_equipo, self.numero)

        return super(RecursoTecnologico, self).save(*args, **kwargs)