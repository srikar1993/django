from django.contrib import admin
from welcomeApp.models import HydJobs

# Register your models here.

class HydJobsAdmin(admin.ModelAdmin):
    jobs_info = ['date', 'company', 'job_title', 'qualification']

admin.site.register(HydJobs, HydJobsAdmin)