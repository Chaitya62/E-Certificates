from django.conf.urls import url
from .views import test, show_certificate


urlpatterns = [
	url(r'^test/$',test, name='test'),
	url(r'^certificate/(?P<certificate_hash>[0-9a-zA-Z]+)/$', show_certificate, name = 'certificate_checker'),

]