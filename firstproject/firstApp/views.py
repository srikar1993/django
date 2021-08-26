from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def welcome(request):
    date = datetime.datetime.now()
    my_dict = {'timestamp': date, 'first_name':'Srikar', 'last_name':'Madhavapeddy'}
    return render(request, 'firstApp/wish.html', context=my_dict)

def home(request):
    return render(request, 'firstApp/home.html')