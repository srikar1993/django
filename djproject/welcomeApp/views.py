from welcomeApp.models import HydJobs
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def welcome_view(request):
    return render(request, 'welcomeApp/index.html')

def hydJobsInfo_view(request):
    jobsinfo = HydJobs.objects.order_by('date')
    my_dict = {'hyd_jobList': jobsinfo}
    return render(request, 'welcomeApp/hyd_jobs.html', context=my_dict)
