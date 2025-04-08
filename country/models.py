from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Country(models.Model):
    short_name = models.CharField(max_length=255)
    long_name = models.CharField(max_length=255)
    west_bound_longitude = models.FloatField(null=True,blank=True)
    east_bound_longitude = models.FloatField(null=True,blank=True)
    south_bound_latitude = models.FloatField(null=True,blank=True)
    north_bound_latitude = models.FloatField(null=True,blank=True)
    crs = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self):
        return f"{self.long_name}"