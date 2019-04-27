from django.contrib import admin

# Register your models here.
from recursos.models import RecursoFisico, RecursoTecnologico, TipoAula, TipoEquipo

class TipoEquipoAdmin(admin.ModelAdmin):
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']

class TipoAulaAdmin(admin.ModelAdmin):
    readonly_fields = ['fecha_creacion', 'fecha_modificacion']

class RecursoFisicoAdmin(admin.ModelAdmin):
    fields = ['tipo_aula', 'numero', 'nombre', 'contenido', 'fecha_creacion', 'fecha_modificacion']
    readonly_fields = ['nombre', 'fecha_creacion', 'fecha_modificacion']

class RecursoTecnologicoAdmin(admin.ModelAdmin):
    fields = ['tipo_equipo', 'numero', 'nombre', 'contenido', 'fecha_creacion', 'fecha_modificacion']
    readonly_fields = ['nombre', 'fecha_creacion', 'fecha_modificacion']

admin.site.register(TipoEquipo, TipoEquipoAdmin)
admin.site.register(TipoAula, TipoAulaAdmin)
admin.site.register(RecursoFisico, RecursoFisicoAdmin)
admin.site.register(RecursoTecnologico, RecursoTecnologicoAdmin)