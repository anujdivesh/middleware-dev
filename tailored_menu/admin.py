from django.contrib import admin
from .models import TailoredMenu
# Register your models here.


class TailoredMenuAdmin(admin.ModelAdmin):
    list_display = ("title","display_title",)

admin.site.register(TailoredMenu,TailoredMenuAdmin)
