
from rest_framework import viewsets, permissions

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from Servicios.models import Ticket, Ticket_Imagen, Ticket_Respuesta, Ticket_Respuesta_Imagen
from Servicios.serializers import TicketSerializer, TicketFullSerializer, TicketImagenFullSerializer, \
    TicketImagenSerializer, TicketRespuestaFullSerializer, TicketRespuestaSerializer, \
    TicketRespuestaImagenFullSerializer, TicketRespuestaImagenSerializer


@permission_classes([IsAuthenticated])
class TicketFullViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('-id')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = TicketFullSerializer

@permission_classes([IsAuthenticated])
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('-id')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = TicketSerializer

@permission_classes([IsAuthenticated])
class TicketImagenFullViewSet(viewsets.ModelViewSet):
    queryset = Ticket_Imagen.objects.all().order_by('-id')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = TicketImagenFullSerializer

@permission_classes([IsAuthenticated])
class TicketImagenViewSet(viewsets.ModelViewSet):
    queryset = Ticket_Imagen.objects.all().order_by('-id')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = TicketImagenSerializer

@permission_classes([IsAuthenticated])
class TicketRespuestaFullViewSet(viewsets.ModelViewSet):
    queryset = Ticket_Respuesta.objects.all().order_by('-id')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = TicketRespuestaFullSerializer

@permission_classes([IsAuthenticated])
class TicketRespuestaViewSet(viewsets.ModelViewSet):
    queryset = Ticket_Respuesta.objects.all().order_by('-id')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = TicketRespuestaSerializer

@permission_classes([IsAuthenticated])
class TicketRespuestaImagenFullViewSet(viewsets.ModelViewSet):
    queryset = Ticket_Respuesta_Imagen.objects.all().order_by('-id')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = TicketRespuestaImagenFullSerializer

@permission_classes([IsAuthenticated])
class TicketRespuestaImagenViewSet(viewsets.ModelViewSet):
    queryset = Ticket_Respuesta_Imagen.objects.all().order_by('-id')
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = TicketRespuestaImagenSerializer




