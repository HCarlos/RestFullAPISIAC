from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

import django.utils.timezone

from django.contrib.auth.models import User


# ---------------------------------------------------------------------------------

# Catálogo de Marcas
class Empleado(models.Model):
    numero_empleado = models.CharField(max_length=100, blank=True, null=True)
    ap_paterno = models.CharField(max_length=100, blank=False, null=False)
    ap_materno = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    curp = models.CharField(max_length=18, blank=True, null=True)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    celulares = models.CharField(max_length=250, blank=True, null=True)
    emails = models.CharField(max_length=500, blank=True, null=True)
    domicilio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['ap_paterno','ap_materno','nombre']

    def __str__(self):
        return'{0} {1} {2}'.format(self.ap_paterno, self.ap_materno, self.nombre)
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('empleado', args=[str(self.id)])


# ---------------------------------------------------------------------------------

# Catálogo de Marcas
class Marca(models.Model):
    marca = models.CharField(max_length=100, unique=True, db_index=True, blank=False, null=False)
    fabricante = models.CharField(max_length=150)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['marca']

    def __str__(self):
        return'{0} - {1}.'.format(self.marca, self.fabricante)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('marca', args=[str(self.id)])


# ---------------------------------------------------------------------------------

# Catálogo de Marcas
class UnidadAdministrativa(models.Model):
    unidad = models.CharField(max_length=250, unique=True, db_index=True, blank=False, null=False)
    abreviatura = models.CharField(max_length=25, unique=True, db_index=True, blank=False, null=False)
    titular = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, related_name='unidadadministrativa_titular')
    modi_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='unidadadministrativa_modi_por')
    modi_el = models.DateTimeField(default=django.utils.timezone.now, blank=True, null=True)

    class Meta:
        verbose_name = 'UnidadAdministrativa'
        verbose_name_plural = 'UnidadesAdministrativas'
        ordering = ['unidad']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('unidad-administrativa', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0} - {1}.'.format(self.unidad, self.abreviatura)


# ---------------------------------------------------------------------------------

# Catálogo de Marcas
class Area(models.Model):
    area = models.CharField(max_length=250, unique=True, db_index=True, blank=False, null=False)
    titular = models.ForeignKey(
        Empleado,
        on_delete=models.SET_NULL,
        null=True,
        related_name='area_titular'
    )
    unidadadministrativa = models.ForeignKey(
        UnidadAdministrativa,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    modi_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='area_modi_por')
    modi_el = models.DateTimeField(default=django.utils.timezone.now, blank=True, null=True)

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'
        ordering = ['area']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('area', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}, {2}'.format(self.area, self.unidadadministrativa, self.titular)



# ---------------------------------------------------------------------------------


    # area = models.ForeignKey(
    #     Area,
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name='equipo_area'
    # )


# Catálogo de Marcas
class Equipo(models.Model):
    TIPO_DISCO_DURO = [
        (1, 'HDD'),
        (2, 'SSD'),
    ]
    c030 = models.IntegerField(default=0, blank=False, null=False)
    unidadadministrativa = models.ForeignKey(UnidadAdministrativa, on_delete=models.SET_NULL, null=True, related_name='equipo_ua')
    equipo = models.CharField(max_length=100, blank=False, null=False)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, related_name='equipo_marca')
    modelo = models.CharField(max_length=250, blank=False, null=False)
    procesador = models.CharField(max_length=250, blank=True, null=True)
    generacion = models.CharField(max_length=100, blank=True, null=True)
    ram = models.CharField(max_length=250, blank=True, null=True)
    discoduro = models.CharField(max_length=250, blank=True, null=True)
    tipodiscoduro = models.SmallIntegerField(choices=TIPO_DISCO_DURO, default=1, blank=True, null=True)
    serie = models.CharField(max_length=100, blank=False, null=False, unique=True)
    inventario = models.CharField(max_length=250, blank=True, null=True)
    inventariomonitor = models.CharField(max_length=30, blank=True, null=True)
    inventariomouse = models.CharField(max_length=30, blank=True, null=True)
    inventarioteclado = models.CharField(max_length=30, blank=True, null=True)
    conexion = models.CharField(max_length=100, blank=True, null=True)
    tiponodo = models.CharField(max_length=100, blank=True, null=True)
    anchobanda = models.CharField(max_length=100, blank=True, null=True)
    numerotelefonico = models.CharField(max_length=100, blank=True, null=True)
    garantia = models.CharField(max_length=100, blank=True, null=True)
    antivirus = models.CharField(max_length=250, blank=True, null=True)
    ofimatica = models.CharField(max_length=250, blank=True, null=True)
    sistemaoperativo = models.CharField(max_length=250, blank=True, null=True)
    empleadoresguardo = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, related_name='equipo_empleadoresguardo')
    observaciones = models.TextField(blank=True, null=True)
    creado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='equipo_creado_por'
    )
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='equipo_modificado_por'
    )
    modidificado_el = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['equipo']
        indexes = [
            models.Index(fields=['c030']),
            models.Index(fields=['serie']),
            models.Index(fields=['inventario']),
            models.Index(fields=['inventariomonitor']),
            models.Index(fields=['inventariomouse']),
            models.Index(fields=['inventarioteclado']),
            models.Index(fields=['tipodiscoduro']),
            models.Index(fields=['marca']),
            models.Index(fields=['empleadoresguardo']),
            models.Index(fields=['unidadadministrativa']),
        ]
        constraints = [
            models.UniqueConstraint(fields=['serie', 'inventario'], name="%(app_label)s_%(class)s_unique")
        ]

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('equipo', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}, {2},  {3}'.format(self.equipo, self.marca, self.modelo, self.empleadoresguardo)





class Area_Equipo(models.Model):
    area = models.ForeignKey(
        Area,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    equipo = models.ForeignKey(
        Equipo,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Area_Equipo'
        verbose_name_plural = 'Area_Equipos'
        ordering = ['area','equipo']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('area-equipo', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}, {2}.'.format(self.id, self.area, self.equipo)



