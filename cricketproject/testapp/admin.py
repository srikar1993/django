from django.contrib import admin
from testapp.models import Cricket

# Register your models here.

class CricketAdmin(admin.ModelAdmin):
    list_display = ['team1', 'team2', 'location', 'victory']

admin.site.register(Cricket, CricketAdmin)