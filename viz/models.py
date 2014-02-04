from django.db import models

class ci(models.Model):
    city = models.CharField(max_length=125)
    state = models.CharField(max_length=125)
    population = models.IntegerField()
    unemployment = models.FloatField()

    def __unicode__(self):
    	return self.city + ', ' + self.state