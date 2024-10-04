
from rest_framework import serializers
from django.contrib.auth.models import User
from drf_writable_nested import WritableNestedModelSerializer

from Home.models import Empleado, Marca, UnidadAdministrativa, Area, Equipo, User, Profile


class UpperCaseSerializerField(serializers.CharField):

    def __init__(self, *args, **kwargs):
        super(UpperCaseSerializerField, self).__init__(*args, **kwargs)

    def to_representation(self, value):
        value = super(UpperCaseSerializerField, self).to_representation(value)
        if value:
            return value.upper()


class UserSerializer(serializers.ModelSerializer):
    # first_name = UpperCaseSerializerField()
    # last_name = UpperCaseSerializerField()
    # def get_full_name(self, obj):
    #     return obj.first_name + ' ' + obj.last_name
    #
    # def get_short_name(self, obj):
    #     return obj.first_name

    class Meta:
        model = User
        fields = [
                    'id','username','email','first_name','last_name'
                ]



# User serial #
class ProfileSerializer(serializers.ModelSerializer):
    # full_name_profile = serializers.SerializerMethodField('get_full_name_profile')
    # short_name_profile = serializers.SerializerMethodField('get_short_name_profile')
    user = UserSerializer(many=False, read_only=False)
    curp = UpperCaseSerializerField()
    rfc = UpperCaseSerializerField()
    domicilio = UpperCaseSerializerField()

    class Meta:
        model = Profile
        fields = ['id','ap_paterno','ap_materno','nombre','curp',
                  'rfc','domicilio','bio','fecha_nacimiento','genero','avatar',
                  'facebook','twitter','linkedin','instagram','github','post','follower','folllowin','user'
                  ]

# Empleado serial
class EmpleadoSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField('get_full_name')
    short_name = serializers.SerializerMethodField('get_short_name')
    ap_paterno = UpperCaseSerializerField()
    ap_materno = UpperCaseSerializerField()
    nombre = UpperCaseSerializerField()
    curp = UpperCaseSerializerField()
    rfc = UpperCaseSerializerField()
    domicilio = UpperCaseSerializerField()
    def get_full_name(self, obj):
        return obj.ap_paterno + ' ' + obj.ap_materno + ' ' + obj.nombre

    def get_short_name(self, obj):
        return obj.nombre + ' ' + obj.ap_paterno

    class Meta:
        model = Empleado
        fields = ['id','ap_paterno','ap_materno','nombre','curp','rfc','celulares','emails','domicilio','numero_empleado','full_name','short_name']

# Marca serial
class MarcaSerializer(serializers.ModelSerializer):
    marca = UpperCaseSerializerField()
    fabricante = UpperCaseSerializerField()
    class Meta:
        model = Marca
        fields = ['id','marca','fabricante','activo']

# Marca serial
class UnidadAdministrativaFullSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    titular = EmpleadoSerializer(many=False, read_only=False)
    unidad = UpperCaseSerializerField()
    abreviatura = UpperCaseSerializerField()
    class Meta:
        model = UnidadAdministrativa
        fields = ['id','unidad','abreviatura','titular']

class UnidadAdministrativaSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    unidad = UpperCaseSerializerField()
    abreviatura = UpperCaseSerializerField()
    class Meta:
        model = UnidadAdministrativa
        fields = ['id','unidad','abreviatura','titular']

# Area serial
class AreaSerializer(serializers.ModelSerializer):
    area = UpperCaseSerializerField()
    class Meta:
        model = Area
        fields = ['id','area','titular','unidadadministrativa']
        depth = 1

# Equipo serial
class EquipoFullSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    empleadoresguardo = EmpleadoSerializer(many=False, read_only=False)
    unidadadministrativa = UnidadAdministrativaSerializer(many=False, read_only=False)
    marca = MarcaSerializer(many=False, read_only=False)
    equipo           = UpperCaseSerializerField()
    serie            = UpperCaseSerializerField()
    modelo           = UpperCaseSerializerField()
    procesador       = UpperCaseSerializerField()
    generacion       = UpperCaseSerializerField()
    ram              = UpperCaseSerializerField()
    discoduro        = UpperCaseSerializerField()
    conexion         = UpperCaseSerializerField()
    tiponodo         = UpperCaseSerializerField()
    anchobanda       = UpperCaseSerializerField()
    antivirus        = UpperCaseSerializerField()
    sistemaoperativo = UpperCaseSerializerField()
    ofimatica        = UpperCaseSerializerField()
    class Meta:
        model = Equipo
        fields = ['id','unidadadministrativa','equipo','marca','modelo','procesador',
                  'generacion','ram','discoduro','serie','inventario','inventariomonitor','inventariomouse',
                  'inventarioteclado','conexion','tiponodo','anchobanda','numerotelefonico','garantia','antivirus',
                  'ofimatica','sistemaoperativo','empleadoresguardo','observaciones']

class EquipoSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    equipo           = UpperCaseSerializerField()
    serie            = UpperCaseSerializerField()
    modelo           = UpperCaseSerializerField()
    procesador       = UpperCaseSerializerField()
    generacion       = UpperCaseSerializerField()
    ram              = UpperCaseSerializerField()
    discoduro        = UpperCaseSerializerField()
    conexion         = UpperCaseSerializerField()
    tiponodo         = UpperCaseSerializerField()
    anchobanda       = UpperCaseSerializerField()
    antivirus        = UpperCaseSerializerField()
    sistemaoperativo = UpperCaseSerializerField()
    ofimatica        = UpperCaseSerializerField()
    class Meta:
        model = Equipo
        fields = ['id','unidadadministrativa','equipo','marca','modelo','procesador',
                  'generacion','ram','discoduro','serie','inventario','inventariomonitor','inventariomouse',
                  'inventarioteclado','conexion','tiponodo','anchobanda','numerotelefonico','garantia','antivirus',
                  'ofimatica','sistemaoperativo','empleadoresguardo','observaciones']

