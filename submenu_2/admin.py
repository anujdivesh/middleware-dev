from django.contrib import admin
from .models import SubMenu2
# Register your models here.


class SubMenu2Admin(admin.ModelAdmin):
    list_display = ("title","display_title",)

admin.site.register(SubMenu2,SubMenu2Admin)
