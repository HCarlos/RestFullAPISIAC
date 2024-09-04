
from rest_framework import viewsets, permissions

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status

from Home.models import Empleado, Marca, UnidadAdministrativa, Area, Equipo
from Home.serializers import UserSerializer, EmpleadoSerializer, MarcaSerializer, UnidadAdministrativaSerializer, \
    AreaSerializer, EquipoSerializer, EquipoFullSerializer, UnidadAdministrativaFullSerializer
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
class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all().order_by('equipo')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = EquipoSerializer

@permission_classes([IsAuthenticated])
class EquipoFullViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all().order_by('equipo')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = EquipoFullSerializer
