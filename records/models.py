from django.db import models

# Create your models here.

class Attendee(models.Model):
	

	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	middle_name = models.CharField(max_length=255)
	

	college = models.CharField(max_length=600)
	email = models.EmailField(max_length=255)


class Event(models.Model):


	event_type = models.CharField(max_length=255)
	event_name = models.CharField(max_length=255)
	event_url = models.CharField(max_length=1000, null=True, blank=True)
	attendees = models.ManyToManyField(Attendee)







