from django.db import models
# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=255)
    enabled = models.BooleanField()

    def __str__(self):
        return f"{self.name}"