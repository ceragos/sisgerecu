# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from talento_humano.models import Empleado, Perfil, CarrreraProfesional, TituloObtenido

admin.site.register(Empleado)
admin.site.register(TituloObtenido)
admin.site.register(CarrreraProfesional)
admin.site.register(Perfil)