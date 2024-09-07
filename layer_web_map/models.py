from django.db import models
from datasets.models import Dataset
# Create your models here.
class LayerWebMap(models.Model):
    enabled = models.BooleanField()
    zoomToLayer = models.BooleanField()
    url = models.CharField(max_length=255)
    layer_title = models.CharField(max_length=255)
    layer_type = models.CharField(max_length=255)
    is_timeseries = models.BooleanField()
    image_format = models.CharField(max_length=255)
    layer_name = models.CharField(max_length=255)
    transparent = models.BooleanField()
    style = models.CharField(max_length=255)
    colormin = models.IntegerField()
    colormax = models.IntegerField()
    abovemaxcolor = models.CharField(max_length=255)
    belowmincolor = models.CharField(max_length=255)
    numcolorbands = models.IntegerField(default=250)
    timeIntervalStart = models.DateTimeField()
    timeIntervalEnd = models.DateTimeField()
    period = models.CharField(max_length=255)
    opacity = models.FloatField(null=True,blank=True)
    legend_url = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.layer_title}"