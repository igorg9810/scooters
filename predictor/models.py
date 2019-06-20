from django.db import models

# Create your models here.

class Conditions(models.Model):
    humidity = models.FloatField()
    timestamp = models.DateTimeField('время')
    temp = models.FloatField()
    felt_temp = models.FloatField()
    wind = models.FloatField()
    holiday = models.BooleanField()
    workday = models.BooleanField()
    season = models.IntegerField()
    weather = models.IntegerField()