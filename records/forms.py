from django import forms
from .models import Event


class CreateNewEvent(forms.ModelForm):
	class Meta():
		model = Event

		fields = ['event_name', 'event_type']
		widgets = {

		'event_type': forms.TextInput(attrs={'class':'form-control '}),
		'event_name': forms.TextInput(attrs={'class':'form-control '})

		}
