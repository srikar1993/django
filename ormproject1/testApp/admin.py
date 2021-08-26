from django.contrib import admin
from testApp.models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'esal', 'ebonus', 'ecity']

admin.site.register(Employee, EmployeeAdmin)
