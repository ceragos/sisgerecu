# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Empleado, Perfil, CarrreraProfesional, TituloObtenido


class EmpleadoAdmin(admin.ModelAdmin):
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']


class TituloObtenidoAdmin(admin.ModelAdmin):
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']


class CarrreraProfesionalAdmin(admin.ModelAdmin):
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']


class PerfilAdmin(admin.ModelAdmin):
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']


admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(TituloObtenido, TituloObtenidoAdmin)
admin.site.register(CarrreraProfesional, CarrreraProfesionalAdmin)
admin.site.register(Perfil, PerfilAdmin)
