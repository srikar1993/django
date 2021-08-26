from django.contrib import admin
from testApp.models import Sports

# Register your models here.

class SportsAdmin(admin.ModelAdmin):
    list_display = ['name', 'players']

admin.site.register(Sports, SportsAdmin)