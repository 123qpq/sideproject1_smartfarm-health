from django.contrib import admin
from .models import farmdata, farminfo

# Register your models here.
class Qadmin(admin.ModelAdmin):
    list_display = ['farmid', 'moisture', 'temperature', 'humidity', 'barometric', 'altitude', 'datetime']
class Iadmin(admin.ModelAdmin):
    list_display = ['farmid', 'toggle']

admin.site.register(farmdata, Qadmin)
admin.site.register(farminfo, Iadmin)
