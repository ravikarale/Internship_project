from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import auth
#from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Company(models.Model):
	CompanyName= models.CharField(max_length=50)
	ContactPerson = models.CharField(max_length=30)
	Desig = models.CharField(max_length=20)
	Phone = models.CharField(max_length=10)
	#Phone=PhoneNumberField()
	#Fax = PhoneNumberField(blank=True)
	Fax = models.CharField(max_length=10)
	Website = models.URLField()
	Email = models.EmailField()
	BriefCompanyProfile = models.CharField(max_length=100)
	
	FinalPosOff=models.CharField(max_length=50)
	FinalNoOfVac=models.IntegerField()
	FinalJobLoc=models.CharField(max_length=50)
	FinalBenefits=models.CharField(max_length=50)
	FinalSelectionProc=models.CharField(max_length=50)

	InternPosOff=models.CharField(max_length=49)
	InternNoOfVac=models.IntegerField()
	InternJobLoc=models.CharField(max_length=50)
	InternBenefits=models.CharField(max_length=50)
	InternSelectionProc=models.CharField(max_length=50)

	FacilityReq=models.CharField(max_length=50)

