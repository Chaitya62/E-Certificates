from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateNewEvent
from .models import Event
from .utils import check_event,generate_event_url


# Create your views here.

def create_event(request):

	if request.method == 'POST':
		form = CreateNewEvent(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Event Created')
	else:
		form = CreateNewEvent()
		url = generate_event_url
		return render(request, 'records/create_event.html',{'title': 'testing', 'form': form, 'url': url})


def view_events(request):

	data = Event.objects.all()
	return render(request, 'records/view.html', {'title': 'view', 'data': data})



def add_participant(request, event, hash):
	if check_event(event, hash):
		return HttpResponse(event + " : "+" hash")


	else: return HttpResponse('404 not found!')



def test(request, te):
	return HttpResponse('sup ? '+te)



