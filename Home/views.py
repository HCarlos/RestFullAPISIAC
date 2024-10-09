
from rest_framework import viewsets, permissions

# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from rest_framework import status

from Home.models import Empleado, Marca, UnidadAdministrativa, Area, Equipo, Subarea, Categoria_de_equipo, Modelo, \
    Color, Condicion, Fuente_de_financiamiento
from Home.serializers import UserSerializer, EmpleadoSerializer, MarcaSerializer, UnidadAdministrativaSerializer, \
    AreaSerializer, EquipoSerializer, EquipoFullSerializer, UnidadAdministrativaFullSerializer, SubareaSerializer, \
    CategoriaDeEquipoSerializer, ModeloSerializer, ColorSerializer, CondicionSerializer, \
    FuenteDeFinanciamientoSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

# Create your views here.
# @authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all().order_by('ap_paterno','ap_materno','nombre')
    # permission_classes = [permissions.AllowAny]
    serializer_class = EmpleadoSerializer

@permission_classes([IsAuthenticated])
class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all().order_by('marca')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = MarcaSerializer

@permission_classes([IsAuthenticated])
class UnidadadministrativaFullViewSet(viewsets.ModelViewSet):
    queryset = UnidadAdministrativa.objects.all().order_by('unidad')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = UnidadAdministrativaFullSerializer

@permission_classes([IsAuthenticated])
class UnidadadministrativaViewSet(viewsets.ModelViewSet):
    queryset = UnidadAdministrativa.objects.all().order_by('unidad')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = UnidadAdministrativaSerializer


@permission_classes([IsAuthenticated])
class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all().order_by('area')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = AreaSerializer

@permission_classes([IsAuthenticated])
class SubareaViewSet(viewsets.ModelViewSet):
    queryset = Subarea.objects.all().order_by('subarea')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubareaSerializer

@permission_classes([IsAuthenticated])
class CategoriaDeEquipoViewSet(viewsets.ModelViewSet):
    queryset = Categoria_de_equipo.objects.all().order_by('categoria')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategoriaDeEquipoSerializer

@permission_classes([IsAuthenticated])
class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all().order_by('modelo')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = ModeloSerializer

@permission_classes([IsAuthenticated])
class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all().order_by('color')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = ColorSerializer

@permission_classes([IsAuthenticated])
class CondicionViewSet(viewsets.ModelViewSet):
    queryset = Condicion.objects.all().order_by('condicion')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = CondicionSerializer

@permission_classes([IsAuthenticated])
class FuenteDeFinanciamientoViewSet(viewsets.ModelViewSet):
    queryset = Fuente_de_financiamiento.objects.all().order_by('fuente_de_financiamiento')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = FuenteDeFinanciamientoSerializer

@permission_classes([IsAuthenticated])
class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all().order_by('equipo')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = EquipoSerializer

@permission_classes([IsAuthenticated])
class EquipoFullViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all().order_by('equipo')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = EquipoFullSerializer
