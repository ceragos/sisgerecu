from django.contrib import admin

from agendas.models import Agenda, Minuta


@admin.register(Agenda)
class AgendasAdmin(admin.ModelAdmin):
    filter_horizontal = ('recurso_tecnologico',)
    list_display = ['nombre_completo', 'recurso_fisico', 'fecha_separacion', 'hora_separacion', 'hora_devolucion']
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']

    def nombre_completo(self, obj):
        return obj.usuario.nombre_completo


@admin.register(Minuta)
class MinutaAdmin(admin.ModelAdmin):
    list_display = ('reserva', 'servicios_generales', 'observacion', 'fecha_creacion', 'fecha_modificacion')
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']
