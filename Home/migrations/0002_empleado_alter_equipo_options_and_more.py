# Generated by Django 5.0.7 on 2024-07-19 19:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_empleado', models.CharField(blank=True, max_length=100, null=True)),
                ('ap_paterno', models.CharField(max_length=100)),
                ('ap_materno', models.CharField(blank=True, max_length=100, null=True)),
                ('nombre', models.CharField(max_length=100)),
                ('curp', models.CharField(blank=True, max_length=18, null=True)),
                ('rfc', models.CharField(blank=True, max_length=13, null=True)),
                ('celulares', models.CharField(blank=True, max_length=250, null=True)),
                ('emails', models.CharField(blank=True, max_length=500, null=True)),
                ('domicilio', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ['ap_paterno', 'ap_materno', 'nombre'],
            },
        ),
        migrations.AlterModelOptions(
            name='equipo',
            options={'ordering': ['unidadadministrativa', 'area'], 'verbose_name': 'Equipo', 'verbose_name_plural': 'Equipos'},
        ),
        migrations.RemoveIndex(
            model_name='equipo',
            name='Home_equipo_usuario_561d61_idx',
        ),
        migrations.RemoveField(
            model_name='equipo',
            name='usuarioresguardo',
        ),
        migrations.AddField(
            model_name='equipo',
            name='empleadoresguardo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipo_empleadoresguardo', to='Home.empleado'),
        ),
        migrations.AlterField(
            model_name='area',
            name='titular',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='area_titular', to='Home.empleado'),
        ),
        migrations.AlterField(
            model_name='unidadadministrativa',
            name='titular',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unidadadministrativa_titular', to='Home.empleado'),
        ),
        migrations.AddIndex(
            model_name='equipo',
            index=models.Index(fields=['c030'], name='Home_equipo_c030_4a55d2_idx'),
        ),
        migrations.AddIndex(
            model_name='equipo',
            index=models.Index(fields=['empleadoresguardo'], name='Home_equipo_emplead_5754a2_idx'),
        ),
    ]
