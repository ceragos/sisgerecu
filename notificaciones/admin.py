from django.contrib import admin

from notificaciones.models import ComunicacionInterna


@admin.register(ComunicacionInterna)
class ComunicacionInternaAdmin(admin.ModelAdmin):
    list_display = ['id', 'remitente', 'destinatario', 'mensaje', 'estado', 'fecha_creacion']
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']
