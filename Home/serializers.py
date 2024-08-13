from rest_framework import serializers
from django.contrib.auth.models import User

from Home.models import Empleado, Marca, UnidadAdministrativa, Area, Equipo

# User serial #
class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField('get_full_name')
    short_name = serializers.SerializerMethodField('get_short_name')
    def get_full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name + ' ' + obj.name

    def get_short_name(self, obj):
        return obj.name + ' ' + obj.first_name

    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','name',
                  'curp','rfc','domicilio','bio','fecha_nacimiento','full_name','short_name',
                  'facebook','twitter','linkedin','instagram','github','post','follower','folllowin']

# Empleado serial
class EmpleadoSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField('get_full_name')
    short_name = serializers.SerializerMethodField('get_short_name')
    def get_full_name(self, obj):
        return obj.ap_paterno + ' ' + obj.ap_materno + ' ' + obj.nombre

    def get_short_name(self, obj):
        return obj.nombre + ' ' + obj.ap_paterno

    class Meta:
        model = Empleado
        fields = ['id','ap_paterno','ap_materno','nombre','curp','rfc','celulares','emails','domicilio','numero_empleado','full_name','short_name']

# Marca serial
class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id','marca','fabricante','activo']

# Marca serial
class UnidadAdministrativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadAdministrativa
        fields = ['id','unidad','abreviatura','titular']

# Area serial
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id','area','titular','unidadadministrativa']

# Equipo serial
class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['id','c030','unidadadministrativa','area','equipo','marca','modelo','procesador',
                  'generacion','ram','discoduro','serie','inventario','inventariomonitor','inventariomouse',
                  'inventarioteclado','conexion','tiponodo','anchobanda','numerotelefonico','garantia','antivirus',
                  'ofimatica','sistemaoperativo','empleadoresguardo']

