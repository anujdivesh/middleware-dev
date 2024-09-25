from django.db import models
from datasets.models import Dataset
from submenu_3.models import SubMenu3
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class SubMenu2(models.Model):
    title = models.CharField(max_length=255)
    display_title = models.CharField(max_length=255,null=True,blank=True)
    content = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    children = models.ManyToManyField(SubMenu3, related_name='submenu3',blank=True)

    def __str__(self):
        return f"{self.title}"