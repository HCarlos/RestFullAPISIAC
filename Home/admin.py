from django.contrib import admin

# Register your models here.

from Home.models import Marca, UnidadAdministrativa, Area, Equipo, Empleado, Area_Equipo, Profile, Subarea, \
    Categoria_de_equipo, Modelo, Color, Condicion, Fuente_de_financiamiento

admin.site.register(Profile)
admin.site.register(Marca)
admin.site.register(UnidadAdministrativa)
admin.site.register(Area)
admin.site.register(Equipo)
admin.site.register(Empleado)
admin.site.register(Area_Equipo)
admin.site.register(Subarea)
admin.site.register(Categoria_de_equipo)
admin.site.register(Modelo)
admin.site.register(Color)
admin.site.register(Condicion)
admin.site.register(Fuente_de_financiamiento)


