from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import auth
from django.db import models

class pcm_auth(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

	def __str__(self):
		self.username



class student(models.Model):
	rollNo = models.IntegerField()
	fName = models.CharField(max_length=20)
	lName = models.CharField(max_length=20)
	

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)