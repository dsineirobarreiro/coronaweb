from django.db import models

from users.models import User

class Event(models.Model):
    name = models.CharField(verbose_name='Name of the event', max_length=64, unique=True)
    date = models.DateField(verbose_name='Date of the event', null=True)

    def __str__(self) -> str:
        return self.name

def event_directory_path(instance, filename): 
    # file will be uploaded to MEDIA_ROOT / corona / <event> / <filename> 
    return 'corona/{0}/{1}'.format(instance.event, filename)

class FileQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for obj in self:
            obj.file.delete()
        super(FileQuerySet, self).delete(*args, **kwargs)

class Memory(models.Model):
    file = models.FileField(verbose_name='Memory of the event', upload_to=event_directory_path)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    objects = FileQuerySet.as_manager()

class Invitation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)