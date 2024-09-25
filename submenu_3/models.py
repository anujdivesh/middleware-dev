from django.db import models
from datasets.models import Dataset
from webapp_product.models import WebProduct
# Create your models here.
class SubMenu3(models.Model):
    title = models.CharField(max_length=255)
    display_title = models.CharField(max_length=255,null=True,blank=True)
    content = models.ManyToManyField(WebProduct, related_name='Content_details',blank=True)

    def __str__(self):
        return f"{self.title}"