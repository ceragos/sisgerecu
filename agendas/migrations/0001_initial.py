# Generated by Django 2.1.2 on 2019-07-14 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recursos', '0004_auto_20190625_1114'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_separacion', models.DateTimeField(verbose_name='Fecha de Separación')),
                ('fecha_devolucion', models.DateTimeField(verbose_name='Fecha de Devolución')),
                ('recurso_fisico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recursos.RecursoFisico', verbose_name='Recurso fisico')),
                ('recurso_tecnologico', models.ManyToManyField(blank=True, null=True, related_name='agenda_recurso', to='recursos.RecursoTecnologico', verbose_name='Recurso Tecnologico')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'agendas',
                'verbose_name_plural': 'agendas',
            },
        ),
    ]