from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from creator.models import Certificate
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt

from creator.models import Certificate

# Create your views here.

def is_logged_in(request):
	return request.user.is_authenticated

def home(request):

	if is_logged_in(request):
		return render(request, 'checker/home.html', {})
	else:

		return HttpResponseRedirect('/login/')


def logout_(request):

	logout(request)
	return HttpResponseRedirect('/login/')

@csrf_exempt
def login_(request):

	if request.method == 'POST':
		username = request.POST.get('username', "")
		password = request.POST.get('password', "")

		user = authenticate(username=username, password=password)

		if user is None:
			return HttpResponseRedirect('/login/')

		login(request, user)

		return HttpResponseRedirect('/home/')

	else:
		if is_logged_in(request):
			return HttpResponseRedirect('/home/')
		return render(request, 'checker/login.html', {})

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
	return render(request, 'creator/certificate.html',{'url': request.build_absolute_uri("/certificate/" + certificate_hash),'name': certificate.certificate_holder.first_name + " " + certificate.certificate_holder.middle_name + " " + certificate.certificate_holder.last_name, 'year': certificate.certificate_holder.year_of_study, 'branch': certificate.certificate_holder.branch, 'event_name': certificate.certificate_event.event_name, 'date': certificate.certificate_event.event_date});

