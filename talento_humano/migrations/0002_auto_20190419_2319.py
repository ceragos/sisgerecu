# Generated by Django 2.1.2 on 2019-04-20 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talento_humano', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='fecha_ingreso',
            field=models.DateField(blank=True, null=True, verbose_name='fecha de ingreso'),
        ),
        migrations.AddField(
            model_name='persona',
            name='edad',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='edad'),
        ),
        migrations.AddField(
            model_name='persona',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True, verbose_name='fecha de nacimiento'),
        ),
    ]