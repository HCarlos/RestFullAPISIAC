from django.contrib import admin

from Servicios.models import Ticket, Ticket_Imagen, Ticket_Respuesta, Ticket_Respuesta_Imagen

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Ticket_Imagen)
admin.site.register(Ticket_Respuesta)
admin.site.register(Ticket_Respuesta_Imagen)
