from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import auth


class pcm(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	email = models.EmailField(default='')

	def __str__(self):
		return self.username



class Students(models.Model):
	rollNo = models.IntegerField()
	firstName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=20)
	emailId = models.EmailField()
	course = models.CharField(max_length=20)
	xth = models.FloatField()
	xiith = models.FloatField()
	graduation = models.FloatField()
	cgpa = models.FloatField()
	status = models.CharField(default='unplace',max_length=20)
	placeType  = models.CharField(default='final', max_length=10)