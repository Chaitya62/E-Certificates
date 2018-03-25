from django.db import models
from records.models import Attendee, Event

# Create your models here.

class Certificate(models.Model):

	certificate_identifier = models.CharField(max_length = 255, unique=True)
	certificate_holder = models.ForeignKey(Attendee, on_delete = models.CASCADE)
	certificate_event = models.ForeignKey(Event, on_delete = models.CASCADE)

	class Meta:
		unique_together = ('certificate_holder', 'certificate_event', )
