from django.contrib import admin
from .models import account

class Qadmin(admin.ModelAdmin):
    list_filter = ['username']
    list_display = ['username']

admin.site.register(account, Qadmin).
