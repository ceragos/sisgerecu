# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from nucleo.models import MarcadorTiempo
from usuarios.models import User


class Persona(models.Model):
    # numero_documento = models.CharField(null=True, blank=False, verbose_name='numero de documento', max_length=40)
    # nombres = models.CharField(null=True, blank=False, verbose_name='nombres', max_length=40)
    # apellidos = models.CharField(null=True, blank=False, verbose_name='apellidos', max_length=40)
    # celular = models.CharField(null=False, blank=False, verbose_name='celular', max_length=40)
    # correo_electronico = models.EmailField(null=True, blank=False, verbose_name='correo electronico', max_length=40)
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name='fecha de nacimiento')
    edad = models.IntegerField(null=True, blank=True, verbose_name='edad', default=0)

    @property
    def calcular_edad(self):
        import datetime

        if type(self.fecha_nacimiento) == type(datetime.datetime.now()):
            self.fecha_nacimiento = self.fecha_nacimiento.date()

        if type(self.fecha_nacimiento) == type(datetime.date.today()):
            age_days = (datetime.date.today() - self.fecha_nacimiento).days
            self.birth_date_year = self.fecha_nacimiento.year
            age = age_days / 365
            if age < 0:
                age = 0
            return age
        elif self.fecha_nacimiento:
            return datetime.date.today().year - self.fecha_nacimiento
        else:
            return 0

    def save(self, *args, **kwargs):
        if self.fecha_nacimiento and not self.edad:
            self.edad = self.calcular_edad

        # if self.nombres:
        #     self.nombres = self.nombres.upper().strip()
        #
        # if self.apellidos:
        #     self.apellidos = self.apellidos.upper().strip()

        return super(Persona, self).save(*args, **kwargs)


class TituloObtenido(MarcadorTiempo):
    nombre = models.CharField(null=True, blank=False, verbose_name='nombre', max_length=40)

    class Meta:
        verbose_name = "titulo"
        verbose_name_plural = "titulos"
        ordering = ['nombre']

    def __str__(self):
        return "%s" % self.nombre


class CarrreraProfesional(MarcadorTiempo):
    nombre = models.CharField(null=True, blank=False, verbose_name='nombre', max_length=40)

    class Meta:
        verbose_name = "carrera"
        verbose_name_plural = "carreras"
        ordering = ['nombre']

    def __str__(self):
        return "%s" % self.nombre


class Perfil(MarcadorTiempo):
    nombre = models.CharField(null=True, blank=False, verbose_name='nombre', max_length=40)

    class Meta:
        verbose_name = "perfil"
        verbose_name_plural = "perfiles"
        ordering = ['nombre']

    def __str__(self):
        return "%s" % self.nombre


class Empleado(MarcadorTiempo, Persona):
    usuario = models.OneToOneField(User, null=False, blank=False, verbose_name='usuario', on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(null=True, blank=True, verbose_name='fecha de ingreso')
    titulo_obtenido = models.ForeignKey(TituloObtenido,  null=True, blank=True, verbose_name='titulo obtenido', on_delete=models.CASCADE)
    carrera_profesional = models.ForeignKey(CarrreraProfesional,  null=True, blank=True, verbose_name='carrera profesional', on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil,  null=True, blank=True, verbose_name='perfil', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "empleado"
        verbose_name_plural = "empleados"
        ordering = ['usuario']

    def __str__(self):
        return "%s %s" % (self.usuario.first_name, self.usuario.last_name)