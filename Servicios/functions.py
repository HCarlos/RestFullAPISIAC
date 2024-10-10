import os
from django.core.exceptions import ValidationError


def upload_path_handler_one(instance, filename):
    import os.path
    fn, ext = os.path.splitext(filename)
    return "tickets/{ticket_id}/{fname}".format(ticket_id=instance.ticket_id, fname=filename)

def upload_path_handler_two(instance, filename):
    import os.path
    fn, ext = os.path.splitext(filename)
    return "tickets/{ticket_id}/{id}/{fname}".format(ticket_id=instance.ticket_id,id=instance.id, fname=filename)


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.pdf', '.xlsx', '.xls', '.doc', '.docx', '.ppt', '.pptx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Ay problemas!!! no soporto ese tipo de archivo!!!')

def file_size(value):
    limit = 500 * (1024 * 1024)
    valor = limit / (1024 * 1024)
    if value.size > limit:
        raise ValidationError('Archivo demasiado pesado. Solo puedes subir archivos de %s gb' % valor)

