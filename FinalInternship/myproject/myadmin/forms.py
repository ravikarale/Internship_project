from django import forms
from myadmin.models import addpcm

class pcmForm(forms.Form):
	class Meta:
		model = addpcm
		fields = ('rollno','name','emailaddress','username','password')