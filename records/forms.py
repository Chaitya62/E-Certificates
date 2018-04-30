from django import forms
from .models import Event,Attendee
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

		yos_choices = (
			('TY', 'Third Year'),
			('SY', 'Second Year'),
			('FY', 'First Year'),
			('B.Tech', 'Final/Fourth Year'),
		)

		branch_choices = (
			('IT', 'Information Technology'),
			('CS', 'Computer Engineering'),
			('MECH', 'Mechnical Engineering'),
			('EXTC', 'Electronics and TeleCommunication'),
			('ETRX', 'Electronics'),
		)

		first_name = forms.CharField(label='First Name',max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
		middle_name = forms.CharField(label='Middle Name', max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
		last_name = forms.CharField(label='Last Name', max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
		division = forms.CharField(label='Division', max_length=1, widget=forms.TextInput(attrs={'class':'form-control'}))
		year_of_study = forms.CharField(label='Year of Study', widget=forms.Select(attrs={'class': 'form-control'}, choices=yos_choices))
		branch = forms.CharField(label='Branch', widget=forms.Select(attrs={'class':'form-control'}, choices=branch_choices))

		college = forms.CharField(label='College Name', max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))
		email = forms.EmailField(label='Email', max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))
