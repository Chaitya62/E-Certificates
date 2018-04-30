
from __future__ import absolute_import
from celery.registry import  tasks
from celery.task import Task
from celery import shared_task


from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage, EmailMultiAlternatives

from django.http import HttpResponse


from records.models import Event



def send_mail(attendee, event):

	subject, from_email, to = 'Here is your certificate', 'codecell.engg@gmail.com',attendee.email

	data = {}

	data['name'] = str(attendee)
	data['year'] = attendee.year_of_study
	data['event_name'] = str(event)
	data['branch'] = attendee.branch
	data['date'] = str(event.event_date)

	html_content = render_to_string('creator/certificate.html', data)

	text_content = strip_tags(html_content)



	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])


	msg.attach_alternative(html_content, "text/html")

	msg.send()

	#return HttpResponse(html_content)


# @shared_task  # Use this decorator to make this a asyncronous function
def generate_certificates(event_id):


	event = Event.objects.get(id=event_id)

	attendees = event.attendees.all()


	for attendee in attendees:
		send_mail(attendee, event)






class TestTask(Task):


	def run(self, test):

		print(test)

		subject, from_email, to = 'Welcome', 'chaitya62gmail.com','chaitya.shah@somaiya.edu'

		html_content = render_to_string('creator/test.html', {'user': 'Chaitya'})

		text_content = strip_tags(html_content)

		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])

		msg.attach_alternative(html_content, "text/html")

		msg.send()


tasks.register(TestTask())
