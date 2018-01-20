from django.conf.urls import url
from .views import test


urlpatterns = [
	url(r'^testing/$',test, name='test')

]