from django.db import models
from webapp_product.models import WebProduct
from country.models import Country
from django.contrib.postgres.fields import ArrayField
from webapp_product.models import WebProduct

# Create your models here.
class Project(models.Model):
    project_code = models.CharField(max_length=255)
    project_name = models.CharField(max_length=500)
    display_title = models.CharField(max_length=255,null=True,blank=True)
    content = models.ManyToManyField(WebProduct, related_name='web_products2',blank=True)

    def __str__(self):
        return f"{self.project_code}"