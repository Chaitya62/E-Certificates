from django.contrib import admin
from .models import Attendee, Event
# Register your models here.

admin.site.register(Attendee)
admin.site.register(Event)
