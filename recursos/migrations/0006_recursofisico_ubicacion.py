# Generated by Django 2.1.2 on 2019-04-27 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0005_auto_20190427_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='recursofisico',
            name='ubicacion',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='ubicación'),
        ),
    ]
