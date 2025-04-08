from django.db import models
from project.models import Project
from country.models import Country
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class TailoredMenu(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    display_title = models.CharField(max_length=255,null=True,blank=True)
    content = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    children = models.ManyToManyField(Project, related_name='projects',blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_id',blank=False)

    def __str__(self):
        return f"{self.title}"