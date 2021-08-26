from testApp.models import Information
from django.shortcuts import render
from django.http import request

# Create your views here.

def welcome(request):
    return render(request, 'testApp/index.html')

def info(request):
    info_list = Information.objects.all()
    my_dict = {'infoList': info_list}
    return render(request, 'testApp/info.html', context=my_dict)