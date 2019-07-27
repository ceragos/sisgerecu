import datetime

from django.db import models


# Create your models here.
class MarcadorTiempo(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.fecha_creacion = datetime.datetime.today()
        else:
            self.fecha_modificacion = datetime.datetime.today()
        super(MarcadorTiempo, self).save(*args, **kwargs)

    class Meta:
        abstract = True
