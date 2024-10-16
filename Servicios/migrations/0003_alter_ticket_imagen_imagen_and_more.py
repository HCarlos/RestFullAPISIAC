# Generated by Django 4.2 on 2024-10-09 23:29

import Servicios.functions
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0002_remove_ticket_imagen_imagen_root_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket_imagen',
            name='imagen',
            field=models.ImageField(blank=True, default=django.utils.timezone.now, upload_to=Servicios.functions.upload_path_handler_one),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ticket_respuesta_imagen',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=Servicios.functions.upload_path_handler_two),
        ),
    ]
