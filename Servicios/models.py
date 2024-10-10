import os

from django.db import models
from django.urls import reverse
from django.utils import timezone

import django.utils.timezone

from django.contrib.auth.models import  User
from django.utils.translation import gettext_lazy as _

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from Home.models import UnidadAdministrativa, Area
from Servicios.functions import upload_path_handler_one, upload_path_handler_two, validate_file_extension, file_size

_UNSAVED_IMAGEFIELD = 'unsaved_imagefield'

# Create your models here.
class Ticket(models.Model):
    TIPO_DE_SOLICITUD = [
        (1, 'Correo electrónico'),
        (2, 'Diseño gráfico impreso'),
        (3, 'Diseño gráfico web'),
        (4, 'Invitación a un evento'),
        (5, 'Publicación web'),
        (6, 'Soporte técnico'),
        (7, 'Solicitud de transparencia'),
        (8, 'Otros'),
    ]
    fecha = models.DateTimeField(default=django.utils.timezone.now, blank=True, null=True)
    fecha_entrega = models.DateTimeField(default=django.utils.timezone.now, blank=True, null=True)
    tipo_de_solicitud = models.SmallIntegerField(choices=TIPO_DE_SOLICITUD, default=1, blank=False, null=False)
    asunto = models.CharField(max_length=250, blank=False, name=False, default="")
    descripcion = models.TextField(blank=False, name=False, default="")
    unidad_administrativa_solicitante = models.ForeignKey(UnidadAdministrativa, on_delete=models.SET_NULL, null=True, related_name='ticket_ua_solicitante')
    area_administrativa_solicitante = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, related_name='ticket_area_admin_solicitante')
    usuario_solicitante = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ticket_usuario_solicitante')
    usuario_responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ticket_usuario_responsable')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        ordering = ['fecha','asunto']

    def __str__(self):
        ua_id = self.unidad_administrativa_solicitante_id
        if isinstance(ua_id, int):
            uao = UnidadAdministrativa.objects.get(pk=ua_id)
            uao = uao.abreviatura
        else:
            uao = ''
        return '{0} {1} {2} {3}'.format(self.id, self.asunto, uao, self.fecha.strftime("%Y-%m-%d %H:%M:%S"))

    @property
    def get_id(self):
        return'{0}'.format(self.id)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('ticket', args=[str(self.id)])

class Ticket_Imagen(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True, related_name='ticket_imagen_ticket')
    fecha = models.DateTimeField(default=django.utils.timezone.now, blank=True, null=True)
    descripcion_imagen = models.CharField(max_length=250, blank=False, name=False, default="")
    usuario_respuesta = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ticket_usuario_respuesta_01')

    imagen = models.ImageField(upload_to=upload_path_handler_one, blank=True, validators=[validate_file_extension, file_size])
    imagen_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ticket_Respuesta'
        verbose_name_plural = 'Imagenes de los Tickets'
        ordering = ['fecha', 'descripcion_imagen']

    def __str__(self):
        return '{0} {1} {2}'.format(self.id, self.fecha.strftime("%Y-%m-%d%H:%M:%S"), self.imagen)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('ticket_usuario_imagen_respuesta', args=[str(self.id)])

    def Imagen(self):
        archivo = upload_path_handler_one
        existe = os.path.isfile(archivo)
        if existe:
            return '/' + str(archivo)
        else:
            return '/media/images/web/file-not-found.jpg'




class Ticket_Respuesta(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True, related_name='ticket_respuesta_ticket')
    fecha = models.DateTimeField(default=django.utils.timezone.now, blank=True, null=True)
    respuesta = models.TextField(blank=False, name=False, default="")
    usuario_respuesta = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ticket_usuario_respuesta')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ticket_Respuesta'
        verbose_name_plural = 'Respuesta a los Tickets'
        ordering = ['fecha', 'respuesta']

    def __str__(self):
        return '{0} {1} {2}'.format(self.id, self.fecha, self.respuesta)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('ticket_usuario_respuesta', args=[str(self.id)])


class Ticket_Respuesta_Imagen(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True, related_name='ticket_respuesta_ticket_id_01')
    ticket_respuesta = models.ForeignKey(Ticket_Respuesta, on_delete=models.SET_NULL, null=True, related_name='ticket_respuesta_id')
    fecha = models.DateTimeField(default=django.utils.timezone.now, blank=True, null=True)
    descripcion_imagen = models.CharField(max_length=250, blank=False, name=False, default="")
    usuario_respuesta = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='ticket_usuario_respuesta_imagen_02')

    imagen = models.ImageField(upload_to=upload_path_handler_two, blank=True, null=True, validators=[validate_file_extension, file_size])
    imagen_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ticket_Respuesta_Imagen'
        verbose_name_plural = 'Imagenes de Respuesta a los Tickets'
        ordering = ['fecha', 'descripcion_imagen']

    def __str__(self):
        return '{0} {1} {2}'.format(self.id, self.fecha, self.respuesta)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('ticket_usuario_imagen_respuesta', args=[str(self.id)])

    def Imagen(self):
        archivo = upload_path_handler_two
        existe = os.path.isfile(archivo)
        if existe:
            return '/' + str(archivo)
        else:
            return '/media/images/web/file-not-found.jpg'




@receiver(pre_save, sender=[Ticket_Imagen, Ticket_Respuesta_Imagen])
def skip_saving_file(sender, instance, **kwargs):
    if not instance.pk and not hasattr(instance, _UNSAVED_IMAGEFIELD):
        setattr(instance, _UNSAVED_IMAGEFIELD, instance.imagen)
        instance.imagen = None

@receiver(post_save, sender=[Ticket_Imagen, Ticket_Respuesta_Imagen])
def update_file_url(sender, instance, created, **kwargs):
    if created and hasattr(instance, _UNSAVED_IMAGEFIELD):
        instance.imagen = getattr(instance, _UNSAVED_IMAGEFIELD)
        instance.save()
