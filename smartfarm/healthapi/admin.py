from django.contrib import admin
from .models import healthdata

class Qadmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display = ['user', 'temperature', 'heartrate', 'datetime']

admin.site.register(healthdata, Qadmin)
# Register your models here.
