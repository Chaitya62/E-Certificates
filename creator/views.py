from django.shortcuts import render
from django.http import HttpResponse

from .tasks import TestTask
from django.core.mail import EmailMessage


# Create your views here.



def test(request):


	TestTask.delay("Hello, World!")



	return HttpResponse("Done!")


