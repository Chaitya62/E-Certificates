from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateNewEvent, CreateNewParticipant
from .models import Event,Attendee
from .utils import check_event,generate_event_url, get_event_by_url
from creator.tasks import generate_certificates


def is_logged_in(request):

	return request.user.is_authenticated



def create_event(request):


	if not is_logged_in(request):
		return HttpResponseRedirect('/login/')

	if request.method == 'POST':
		form = CreateNewEvent(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/home/')
		return HttpResponse('It Failed')
	else:
		form = CreateNewEvent()
		return render(request, 'records/create_event.html',{'title': 'testing', 'form': form})





def view_events(request):

	if not is_logged_in(request):
		return HttpResponseRedirect('/login/')


	if request.method == 'GET':
		data = Event.objects.all()
		return render(request, 'records/view.html', {'title': 'view', 'data': data})
	elif request.method == 'POST':
		data = request.POST.get('event_url')
		event = get_event_by_url(data)
		attendees = event.attendees.all()
		event_id = request.POST.get('event_id')
		generate_certificates(event_id, request)
		# request certificate generation here(async)
		# try to use celery here
		return HttpResponse("Done")


def view_participants(request):

	if not is_logged_in(request):
		return HttpResponseRedirect('/login/')

	data = Attendee.objects.all()
	return render(request, 'records/view_participants.html', {'title': 'Attendees', 'data': data})

def view_attendees(request, event, hash):

	if not is_logged_in(request):
		return HttpResponseRedirect('/login/')


	url = generate_event_url(event)
	event =  get_event_by_url(url)
	data = event.attendees.all()

	return render(request, 'records/view_participants.html', {'title': 'Attendees', 'data': data})


def add_participant(request, event, hash):
	if check_event(event, hash):
		if request.method == 'POST':
			form = CreateNewParticipant(request.POST)

			if(form.is_valid()):
				# print(form.fields)
				p = Attendee(**form.cleaned_data)
				p.save()
				url = generate_event_url(event)
				event =  get_event_by_url(url)

				event.attendees.add(p)


				#for field in data.keys():

				#p.save()
				return HttpResponse('done!!!')
			return HttpResponse("Failed ....")

		elif request.method == 'GET':
			form = CreateNewParticipant(request.POST)

			return render(request, 'records/add_participant.html', {'title': 'Redeem you certificate', 'form': form})




	else:
		return HttpResponse('404 not found!')



def test(request, te):
	return HttpResponse('sup ? '+te)
