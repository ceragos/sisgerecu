from django.contrib import admin

from notificaciones.models import ComunicacionInterna


@admin.register(ComunicacionInterna)
class ComunicacionInternaAdmin(admin.ModelAdmin):
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']
