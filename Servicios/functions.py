
def upload_path_handler_one(instance, filename):
    import os.path
    fn, ext = os.path.splitext(filename)
    return "tickets/{ticket_id}/{fname}".format(ticket_id=instance.ticket_id, fname=filename)

def upload_path_handler_two(instance, filename):
    import os.path
    fn, ext = os.path.splitext(filename)
    return "tickets/{ticket_id}/{id}/{fname}".format(ticket_id=instance.ticket_id,id=instance.id, fname=filename)



