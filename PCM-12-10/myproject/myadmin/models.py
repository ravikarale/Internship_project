from __future__ import unicode_literals

from django.db import models

# Create your models here.
class addpcm(models.Model):
	rollno=models.CharField(max_length=120)
	name=models.CharField(max_length=120)
	emailaddress=models.EmailField(max_length=30)
	username=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
