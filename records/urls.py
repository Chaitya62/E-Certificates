from django.conf.urls import url
from .views import create_event,view_events,add_participant, view_participants,view_attendees


urlpatterns = [

	url(r'^event/create/$',create_event, name='create_event'),
	url(r'^event/view/$', view_events, name='view_events'),
	url(r'^event/(?P<event>[a-zA-Z \?\.\, \+]+)/(?P<hash>[0-9a-zA-Z]+)/$', add_participant, name='test'),
	url(r'^event/attendees/$', view_participants, name='view_participants'),
	url(r'^event/(?P<event>[a-zA-Z\?\.\, \+]+)/(?P<hash>[0-9a-zA-Z]+)/view/$', view_attendees, name='view_attendees')	
]