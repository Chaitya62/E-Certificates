from django.shortcuts import render
from django.http import HttpResponse

from creator.models import Certificate

# Create your views here.

def test(request):
	return HttpResponse("Hello, World!")

def show_certificate(request, certificate_hash):
	certificate = ""
	try:
		certificate = Certificate.objects.get(certificate_identifier = certificate_hash)
	except Certificate.DoesNotExist:
		return HttpResponse("404 Not Found")
	except Certificate.MultipleObjectsReturned:
		print("This is impossible")
		return HttpResponse("400 Bad Request")
	except:
		print("Don't expect this")

	# No views yet
	string_to_show = "Name: " + certificate.certificate_holder.first_name + " " + certificate.certificate_holder.middle_name + " " + certificate.certificate_holder.last_name
	string_to_show = string_to_show + "<br>College: " + certificate.certificate_holder.college + "<br>Email: " + certificate.certificate_holder.email
	string_to_show = string_to_show + "<br>Event Name: " + certificate.certificate_event.event_name
	return render(request, 'view_cert.html',{'title': certificate.certificate_event.event_name, 'event_name': certificate.certificate_event.event_name, 'name': certificate.certificate_holder.first_name + " " + certificate.certificate_holder.middle_name + " " + certificate.certificate_holder.last_name, 'email': certificate.certificate_holder.email, 'college': certificate.certificate_holder.college})
