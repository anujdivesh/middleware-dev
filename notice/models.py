from django.db import models
# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=255)
    description_enabled = models.BooleanField(default=True)
    description = models.TextField(null=True,blank=True)
    image_enabled = models.BooleanField(default=True)
    image = models.ImageField(upload_to='notice/',null=True,blank=True)
    url_enabled = models.BooleanField(default=True)
    url = models.URLField(max_length=2000,null=True,blank=True)
    is_notice_enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"
