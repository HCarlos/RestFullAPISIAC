# Generated by Django 4.2 on 2024-10-10 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_remove_area_titular_subarea_modelo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unidadadministrativa',
            options={'ordering': ['unidad'], 'verbose_name': 'Unidad Administrativa', 'verbose_name_plural': 'Unidades Administrativas'},
        ),
        migrations.AlterField(
            model_name='area',
            name='area',
            field=models.CharField(db_index=True, max_length=250),
        ),
    ]
