# Generated by Django 2.1.2 on 2019-04-27 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0007_auto_20190427_0116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recursotecnologico',
            old_name='referecia',
            new_name='refenrecia',
        ),
    ]