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

    class Meta:
        verbose_name = 'recurso'
        verbose_name_plural = 'recursos'


class RecursoFisico(MarcadorTiempo, Recurso):
    tipo_aula = models.ForeignKey(TipoAula, null=True, blank=True, verbose_name='tipo de aula',on_delete=models.CASCADE)
    nombre = models.CharField(max_length=40, null=True, blank=True, verbose_name='nombre', unique=True)

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

    class Meta:
        verbose_name = 'recurso fisico'
        verbose_name_plural = 'recursos fisicos'
        ordering = ['nombre']

    def __str__(self):
        return '%s' % self.nombre

    def save(self, *args, **kwargs):
        if not self.nombre:
            self.nombre = '%s %s' % (self.tipo_equipo, self.numero)

        return super(RecursoTecnologico, self).save(*args, **kwargs)