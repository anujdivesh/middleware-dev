from django.contrib import admin
from .models import SubMenu3
# Register your models here.


class SubMenu3Admin(admin.ModelAdmin):
    list_display = ("title",)

admin.site.register(SubMenu3,SubMenu3Admin)
