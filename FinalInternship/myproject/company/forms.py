from django import forms

from pcm.models import  Students


class StudentsForm(forms.Form):
	class Meta:
		model = Students
		fields = ('rollNo','firstName','lastName','emailId','course','xth','xiith','graduation','cgpa','status','type')

# class CompanyRegForm(forms.Form):
# 	companyName = CharField(max_length=50)
# 	contactPersion = CharField(max_length=20)
# 	designation = CharField(max_length=50)
# 	phoneNumber = RegexField(regex=r'^\+?1?\d{9,15}$', error_message = ("Phone number must be entered in the format:"))
# 	phoneNumber = PhoneNumberField()
#     faxNumber = PhoneNumberField(blank=True)
#     webSite = UrlField()
#     emailId = EmailField()
#     brifCompnyProf = CharField(max_length=100)
