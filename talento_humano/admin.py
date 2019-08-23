# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Empleado, Perfil, CarrreraProfesional, TituloObtenido


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']


@admin.register(TituloObtenido)
class TituloObtenidoAdmin(admin.ModelAdmin):
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']


@admin.register(CarrreraProfesional)
class CarrreraProfesionalAdmin(admin.ModelAdmin):
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']
