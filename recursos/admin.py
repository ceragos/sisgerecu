from django.contrib import admin

# Register your models here.
from recursos.models import RecursoFisico, RecursoTecnologico, TipoAula, TipoEquipo, GaleriaRecursoFisico, \
    GaleriaRecursoTecnologico


class TipoEquipoAdmin(admin.ModelAdmin):
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']

class TipoAulaAdmin(admin.ModelAdmin):
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']

class RecursoFisicoAdmin(admin.ModelAdmin):
    fields = ['tipo_aula', 'numero', 'nombre', 'ubicacion', 'capacidad', 'caracteristicas', 'contenido', 'fecha_creacion', 'fecha_modificacion']
    readonly_fields = ['nombre', 'fecha_creacion', 'fecha_modificacion']

class RecursoTecnologicoAdmin(admin.ModelAdmin):
    fields = ['tipo_equipo', 'numero', 'nombre', 'marca', 'referencia', 'color', 'caracteristicas', 'contenido', 'fecha_creacion', 'fecha_modificacion']
    readonly_fields = ['nombre', 'fecha_creacion', 'fecha_modificacion']

class GaleriaRecursoFisicoAdmin(admin.ModelAdmin):
    fields = ['recurso_fisico', 'imagen', 'fecha_creacion', 'fecha_modificacion']
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']

class GaleriaRecursoTecnologicoAdmin(admin.ModelAdmin):
    fields = ['recurso_tecnologico', 'imagen', 'fecha_creacion', 'fecha_modificacion']
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']

admin.site.register(TipoEquipo, TipoEquipoAdmin)
admin.site.register(TipoAula, TipoAulaAdmin)
admin.site.register(RecursoFisico, RecursoFisicoAdmin)
admin.site.register(RecursoTecnologico, RecursoTecnologicoAdmin)
admin.site.register(GaleriaRecursoFisico, GaleriaRecursoFisicoAdmin)
admin.site.register(GaleriaRecursoTecnologico, GaleriaRecursoTecnologicoAdmin)