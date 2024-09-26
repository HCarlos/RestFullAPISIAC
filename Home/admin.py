from django.contrib import admin

# Register your models here.

from Home.models import Marca, UnidadAdministrativa, Area, Equipo, Empleado, Area_Equipo, Profile

admin.site.register(Profile)
admin.site.register(Marca)
admin.site.register(UnidadAdministrativa)
admin.site.register(Area)
admin.site.register(Equipo)
admin.site.register(Empleado)
admin.site.register(Area_Equipo)
