from celery.registry import  tasks
from celery.task import Task


from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

class TestTask(Task):


	def run(self, test):

		print(test)

		subject, from_email, to = 'Welcome', 'chaitya62gmail.com','chaitya.shah@somaiya.edu'

		html_content = render_to_string('creator/test.html', {'user': 'Chaitya'})

		text_content = strip_tags(html_content)

		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])

		msg.attach_alternative(html_content, "text/html")

		msg.send()


tasks.register(TestTask())