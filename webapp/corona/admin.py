from django.contrib import admin

from .models import Event, Memory, Invitation

# Register your models here.
admin.site.register(Event, list_display=('name', 'date'))
admin.site.register(Memory, list_display=('file', 'event'))
admin.site.register(Invitation, list_display=('user', 'event'))