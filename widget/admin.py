from django.contrib import admin
from .models import Widget
# Register your models here.


class WidgetAdmin(admin.ModelAdmin):
    list_display = ("title","display_title",)

admin.site.register(Widget,WidgetAdmin)
