from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuarios.models import User

class CustomUserAdmin(UserAdmin):
    filter_horizontal = ('groups',)
    def __init__(self, *args, **kwargs):
        super(UserAdmin, self).__init__(*args, **kwargs)

        UserAdmin.fieldsets = list(UserAdmin.fieldsets) + [(None, {'fields': ('numero_documento', 'celular')})]

        # UserAdmin.list_display = list(UserAdmin.list_display) + ['numero_documento', 'celular']

    def save_model(self, request, obj, form, change):
        # obj.creado_por = request.user
        super(CustomUserAdmin, self).save_model(request, obj, form, change)

admin.site.register(User, CustomUserAdmin)