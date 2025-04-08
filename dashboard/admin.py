from django.contrib import admin
from .models import Dashboard
# Register your models here.


class DashboardAdmin(admin.ModelAdmin):
    list_display = ("title","display_title",)

admin.site.register(Dashboard,DashboardAdmin)
