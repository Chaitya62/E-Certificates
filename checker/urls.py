from django.conf.urls import url
from .views import test, show_certificate, home, login_, logout_


urlpatterns = [
	url(r'^test/$',test, name='test'),
	url(r'^certificate/(?P<certificate_hash>[0-9a-zA-Z]+)/$', show_certificate, name = 'certificate_checker'),
	url(r'^home/$', home, name='home'),
	url(r'^login/$', login_, name='login'),
	url(r'^logout/$', logout_, name='logout')

]
