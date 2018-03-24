import hashlib
from .models import Event


def check_event(event, hash):

	event = event.encode(encoding='ASCII')
	actual_hash = hashlib.md5(event)
	actual_hash = actual_hash.hexdigest()
	return hash == actual_hash


def prepare_event_for_hash(event_name):
	return ''.join([i.lower() for i in list(event_name) if (i.strip()) != ''])


def generate_event_url(event_name):

	url = '/event/'
	event_name = prepare_event_for_hash(event_name)
	url+=event_name+'/'
	url+=(hashlib.md5(event_name.encode(encoding='ASCII')).hexdigest())
	url+='/'

	return url


def get_event_by_url(event_url):

	data = Event.objects.get(event_url=event_url)
	return data

