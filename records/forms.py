from django import forms
from .models import Event
from .utils import generate_event_url

class CreateNewEvent(forms.ModelForm):
	class Meta():
		model = Event

		fields = ['event_name', 'event_type', 'event_url']
		widgets = {

		'event_type': forms.TextInput(attrs={'class':'form-control ', }),
		'event_name': forms.TextInput(attrs={'class':'form-control '}),
		'event_url': forms.HiddenInput()		

		}




	def clean_event_url(self):
		data = self.cleaned_data['event_url']

		event_ = self.cleaned_data['event_name']

		data = generate_event_url(event_)

		return data


