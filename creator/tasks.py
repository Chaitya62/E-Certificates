
from __future__ import absolute_import
from celery.registry import  tasks
from celery.task import Task
from celery import shared_task


from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.utils.crypto import get_random_string

from django.http import HttpResponse
from django.http import HttpRequest
from django.db import IntegrityError


from records.models import Event
from creator.models import Certificate
from creator.utils import generate_hash



def send_mail(attendee, event, certificate, request):

	subject, from_email, to = 'Here is your certificate', 'codecell.engg@gmail.com',attendee.email

	text_content = "Hello, " + attendee.first_name + "<br><br>&emsp;Your certificate for " + event.event_name + " is ready." + "<br>&emsp;You can view and verify your certificate at : " + request.build_absolute_uri("/certificate/" + certificate.certificate_identifier) + "<br>&emsp;You can download your certificate at: " + request.build_absolute_uri("/certificate/" + certificate.certificate_identifier + "/?download=true");

	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])

	msg.attach_alternative(text_content, "text/html")

	msg.send()

	# return HttpResponse(html_content)


# @shared_task  # Use this decorator to make this a asyncronous function
def generate_certificates(event_id, request):


	event = Event.objects.get(id=event_id)

	attendees = event.attendees.all()


	for attendee in attendees:
		for attendee in event.attendees.all():
			# Now generate model
			try:
				print(event.event_name + " " + event.event_url)
				certificate = Certificate(certificate_identifier = get_random_string(length = 7), certificate_holder = attendee, certificate_event = event)
				certificate.save()
				send_mail(attendee, event, certificate, request)
			except IntegrityError:
				print("Already Created Certificate For This User")
			except:
				print("Something was wrong with certificate generation for a user, ignored..")






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
