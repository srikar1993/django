from django.contrib import admin
from testApp.models import Innovation

# Register your models here.

class InnovationAdmin(admin.ModelAdmin):
    list_display = ['innovation', 'innovator', 'year']

admin.site.register(Innovation, InnovationAdmin)