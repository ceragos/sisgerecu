# Generated by Django 2.1.2 on 2019-08-14 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agendas', '0003_remove_agenda_fecha_devolucion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='recurso_fisico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recursos.RecursoFisico', verbose_name='recurso físico'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='recurso_tecnologico',
            field=models.ManyToManyField(blank=True, help_text='Mantenga presionado "Control" o "Command" en un Mac, para seleccionar más de una opción.', related_name='agenda_recurso', to='recursos.RecursoTecnologico', verbose_name='recurso tecnólogico'),
        ),
    ]
