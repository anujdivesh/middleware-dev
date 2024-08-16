from django.contrib import admin
from .models import TaskDownload
# Register your models here.


class TaskDownloadAdmin(admin.ModelAdmin):
    list_display = ("task_name", "class_id", "status","status",)

admin.site.register(TaskDownload,TaskDownloadAdmin)
