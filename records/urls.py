from django.conf.urls import url
from .views import create_event,view_events,add_participant


urlpatterns = [

	url(r'^event/create/$',create_event, name='create_event'),
	url(r'^event/view/$', view_events, name='view_events'),
	url(r'^event/(?P<event>[a-zA-Z\+]+)/(?P<hash>[0-9a-zA-Z]+)/$', add_participant, name='test')
	
]