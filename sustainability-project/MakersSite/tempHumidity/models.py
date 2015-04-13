from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class tempHumidity(models.Model):
	pi_num = models.IntegerField()
	temperature = models.FloatField()
	humidity = models.FloatField()
	date_rec = models.DateTimeField('date published')
	def __str__(self): 
		return "Pi Id: " + str(self.pi_num) + " Temperature: " + str(self.temperature) + " Humidity: " + str(self.humidity)
