from django.db import models
import datetime
from django import forms

class UserName(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	github = models.CharField(max_length=50)
	join_date = models.DateTimeField('date published')
	def __str__(self): 
		return self.first_name +" "+self.last_name
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=5) <= self.pub_date <= now