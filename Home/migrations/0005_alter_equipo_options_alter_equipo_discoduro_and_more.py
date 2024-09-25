# Generated by Django 5.0.7 on 2024-07-20 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_alter_marca_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipo',
            options={'ordering': ['equipo'], 'verbose_name': 'Equipo', 'verbose_name_plural': 'Equipos'},
        ),
        migrations.AlterField(
            model_name='equipo',
            name='discoduro',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='generacion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='procesador',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='ram',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
