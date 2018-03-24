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




class CreateNewParticipant(forms.Form):
		first_name = forms.CharField(label='First Name',max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
		middle_name = forms.CharField(label='Middle Name', max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
		last_name = forms.CharField(label='Last Name', max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))

		college = forms.CharField(label='College Name', max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))
		email = forms.EmailField(label='Email', max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))

