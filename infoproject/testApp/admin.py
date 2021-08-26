from django.contrib import admin
from testApp.models import Information

# Register your models here.

class InformationAdmin(admin.ModelAdmin):
    my_list = ['name', 'email', 'phone', 'address']

admin.site.register(Information, InformationAdmin)