from django.db import models
from datasets.models import Dataset
# Create your models here.
class LayerWebMap(models.Model):
    enabled = models.BooleanField()
    zoomToLayer = models.BooleanField()
    url = models.CharField(max_length=255)
    on_click_url = models.CharField(max_length=255,null=True,blank=True)
    layer_title = models.CharField(max_length=255)
    layer_type = models.CharField(max_length=255)
    is_timeseries = models.BooleanField()
    datetime_format = models.CharField(max_length=255)
    image_format = models.CharField(max_length=255)
    layer_name = models.CharField(max_length=255)
    transparent = models.BooleanField()
    update_transparency = models.BooleanField()
    style = models.CharField(max_length=255)
    colormin = models.IntegerField()
    colormax = models.IntegerField()
    update_color = models.BooleanField()
    abovemaxcolor = models.CharField(max_length=255)
    belowmincolor = models.CharField(max_length=255)
    numcolorbands = models.IntegerField(default=250)
    timeIntervalStart = models.DateTimeField()
    timeIntervalEnd = models.DateTimeField()
    period = models.CharField(max_length=255)
    opacity = models.FloatField(null=True,blank=True)
    legend_url = models.CharField(max_length=255)
    update_legend = models.BooleanField()
    is_composite = models.BooleanField()
    generate_png = models.BooleanField()
    enable_chart = models.BooleanField()
    chart_style = models.CharField(max_length=255,null=True,blank=True)
    has_height = models.BooleanField()
    has_depth = models.BooleanField()
    update_thredds = models.BooleanField()

    def __str__(self):
        return f"{self.layer_title}"