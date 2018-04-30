from django.db import models

from datetime import datetime
# Create your models here.



class Attendee(models.Model):


	yos_choices = (
	('TY', 'Third Year'),
	('SY', 'Second Year'),
	('FY', 'First Year'),
	('B.Tech', 'Final/Fourth Year'),
	)

	branch_choices = (
	('IT', 'Information Technologies'),
	('CS', 'Computer Engineering'),
	('MECH', 'Mechnical Engineering'),
	('EXTC', 'Electronics and TeleCommunication'),
	('ETRX', 'Electronics'),
	)


	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	middle_name = models.CharField(max_length=255)
	year_of_study = models.CharField(max_length=255, choices=yos_choices,default='FY', blank=True)
	branch = models.CharField(max_length=255, choices=branch_choices,default='IT', blank=True)
	division = models.CharField(max_length=255, default='A', blank=True)


	college = models.CharField(max_length=600)
	email = models.EmailField(max_length=255)



	def __str__(self):
		return "%s %s %s" % (self.first_name, self.middle_name, self.last_name)



class Event(models.Model):


	event_type = models.CharField(max_length=255)
	event_name = models.CharField(max_length=255)
	event_date = models.DateField(default=datetime.now)
	event_url = models.CharField(max_length=1000, null=True, blank=True)
	attendees = models.ManyToManyField(Attendee)


	def __str__(self):

		return "%s"%(self.event_name)
