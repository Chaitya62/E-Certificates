from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError

from .tasks import TestTask, generate_certificate
from django.core.mail import EmailMessage
from records.models import Event, Attendee
from records.utils import generate_event_url, get_event_by_url
from .utils import generate_hash
from .models import Certificate



# Create your views here.



def test(request):


	# email = EmailMessage('title', 'body', to=['chaitya.shah@somaiya.edu'])
	# email.send()


	generate_certificate.delay("Hello, World!")





	return HttpResponse("Done!")



def certificate(request):

	return render(request, 'creator/certificate.html')


def make_cert(request, event_name):

	if request.method == 'GET':

		event_url = generate_event_url(event_name)
		event = get_event_by_url( event_url )

		for attendee in event.attendees.all():
			# Now generate model
			try:
				certificate = Certificate(certificate_identifier = generate_hash(attendee, event_name, event_url), certificate_holder = attendee, certificate_event = event)
				certificate.save()
			except IntegrityError:
				print("Already Created Certificate For This User")
			except:
				print("Something is wrong")
				# Yet to decide what to do. Maybe nothing

		return HttpResponse("Welcome! ")
