from rest_framework import serializers

from Home.serializers import UserSerializer, UnidadAdministrativaSerializer, AreaSerializer
from Servicios.models import Ticket, Ticket_Imagen, Ticket_Respuesta, Ticket_Respuesta_Imagen


# ---------------------- TICKET SERIALIZER --------------------------------
class TicketFullSerializer(serializers.ModelSerializer):
    ua = UnidadAdministrativaSerializer(many=False, read_only=False)
    area = AreaSerializer(many=False, read_only=False)
    solicitante = UserSerializer(many=False, read_only=False)
    responsable = UserSerializer(many=False, read_only=False)

    class Meta:
        model = Ticket
        fields = [
            'id','fecha','fecha_entrega','tipo_de_solicitud','asunto','descripcion',
            'ua','area','solicitante','responsable',
            ]

class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = [
            'id','fecha','fecha_entrega','tipo_de_solicitud','asunto','descripcion',
            'unidad_administrativa_solicitante','area_administrativa_solicitante','usuario_solicitante','usuario_responsable',
            ]


# ----------------------------------------------------------------

# ---------------------- TICKET IMAGEN SERIALIZER --------------------------------
class TicketImagenFullSerializer(serializers.ModelSerializer):
    ticket = TicketSerializer(many=False, read_only=False)

    class Meta:
        model = Ticket_Imagen
        fields = [
            'id','ticket','fecha','descripcion_imagen','usuario_respuesta','imagen',
            ]

class TicketImagenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket_Imagen
        fields = [
            'id','ticket','fecha','descripcion_imagen','usuario_respuesta','imagen',
            ]


# ----------------------------------------------------------------

# ---------------------- TICKET RESPUESTA SERIALIZER --------------------------------
class TicketRespuestaFullSerializer(serializers.ModelSerializer):
    ticket = TicketSerializer(many=False, read_only=False)

    class Meta:
        model = Ticket_Respuesta
        fields = [
            'id','ticket','fecha','respuesta','usuario_respuesta',
            ]

class TicketRespuestaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket_Respuesta
        fields = [
            'id','ticket','fecha','respuesta','usuario_respuesta',
            ]


# ----------------------------------------------------------------

# ---------------------- TICKET IMAGEN SERIALIZER --------------------------------
class TicketRespuestaImagenFullSerializer(serializers.ModelSerializer):
    ticket = TicketSerializer(many=False, read_only=False)
    ticket_respuesta = TicketRespuestaSerializer(many=False, read_only=False)

    class Meta:
        model = Ticket_Respuesta_Imagen
        fields = [
            'id','ticket','ticket_respuesta','fecha','descripcion_imagen','usuario_respuesta','imagen',
            ]

class TicketRespuestaImagenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket_Respuesta_Imagen
        fields = [
            'id','ticket','ticket_respuesta','fecha','descripcion_imagen','usuario_respuesta','imagen',
            ]


# ----------------------------------------------------------------

