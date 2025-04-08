from django.db import models
from project.models import Project
from country.models import Country
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Dashboard(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    display_title = models.CharField(max_length=255,null=True,blank=True)
    access_url = models.CharField(max_length=255,null=True,blank=True)
    display_image_url = models.CharField(max_length=255,null=True,blank=True)
    publicly_available = models.BooleanField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='dashboard_id',blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='dashboard_id',blank=False)
    maintainer = models.CharField(max_length=255,null=True,blank=True)
    maintainer_contact = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f"{self.title}"