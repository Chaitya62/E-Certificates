from django.conf.urls import url

from .views import test, make_cert

urlpatterns = [
	url(r'^check/$',test, name='test'),
	url(r'^make_user_certificate/(?P<event_name>[0-9a-zA-Z]+)/$', make_cert, name = 'make_certificates'),
]
