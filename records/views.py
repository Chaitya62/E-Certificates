from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateNewEvent
from .models import Event
from .utils import check_event,generate_event_url


def create_event(request):

	if request.method == 'POST':
		form = CreateNewEvent(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Event Created')
		return HttpResponse('It Failed')
	else:
		form = CreateNewEvent()
		return render(request, 'records/create_event.html',{'title': 'testing', 'form': form})


def view_events(request):

	data = Event.objects.all()
	return render(request, 'records/view.html', {'title': 'view', 'data': data})



def add_participant(request, event, hash):
	if check_event(event, hash):
		return HttpResponse(event + " : "+ hash)


	else: return HttpResponse('404 not found!')



def test(request, te):
	return HttpResponse('sup ? '+te)



