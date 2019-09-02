from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    foto_perfil = models.ImageField(upload_to='usuarios/perfil', null=True, blank=True, verbose_name='foto de perfil')
    numero_documento = models.CharField(null=True, blank=False, verbose_name='numero de documento', max_length=40)
    celular = models.CharField(null=False, blank=False, verbose_name='celular', max_length=40)
    codigo_verificacion = models.CharField(null=True, blank=True, verbose_name='codigo de verificación', max_length=4)
    fecha_solicitud_codigo_verificacion = models.DateTimeField(null=True, blank=True,
                                                               verbose_name='ultima fecha en que solicito el codigo')

    class Meta:
        unique_together = ('email',)
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        permissions = (
            ('es_administrativo', 'Perfil administrativo'),
            ('es_docente', 'Perfil docente'),
            ('es_servicios_generales', 'Perfil servicios generales'),
        )

    def __str__(self):
        return self.nombre_completo

    def save(self, *args, **kwargs):
        return super(User, self).save(*args, **kwargs)

    @property
    def nombre_completo(self):
        return "%s %s" % (self.first_name, self.last_name)
