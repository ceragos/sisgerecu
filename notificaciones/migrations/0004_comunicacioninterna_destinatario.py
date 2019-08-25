# Generated by Django 2.1.2 on 2019-08-25 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notificaciones', '0003_auto_20190824_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunicacioninterna',
            name='destinatario',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, related_name='destinatario_usuario', to=settings.AUTH_USER_MODEL, verbose_name='destinatario'),
            preserve_default=False,
        ),
    ]
