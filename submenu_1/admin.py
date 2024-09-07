from django.contrib import admin
from .models import SubMenu1
# Register your models here.


class SubMenu1Admin(admin.ModelAdmin):
    list_display = ("title",)

admin.site.register(SubMenu1,SubMenu1Admin)
