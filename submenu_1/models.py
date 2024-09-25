from django.db import models
from datasets.models import Dataset
from webapp_product.models import WebProduct
from submenu_2.models import SubMenu2
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class SubMenu1(models.Model):
    title = models.CharField(max_length=255)
    display_title = models.CharField(max_length=255,null=True,blank=True)
    content = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    children = models.ManyToManyField(SubMenu2, related_name='submenu2',blank=True)