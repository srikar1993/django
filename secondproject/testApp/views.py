from django.shortcuts import render
from django.http import HttpRequest
import datetime

# Create your views here.

def dateinfo(request):

    date = datetime.datetime.now()
    my_dict = {'timestamp': date, 'name': 'Srikar Madhavapeddy', 'age': 27}
    return render(request, 'testApp/index.html', context=my_dict)

def greeting(request):

    date = datetime.datetime.now()
    hour = int(date.strftime('%H'))
    msg = ''
    if hour >= 6 and hour < 12:
        msg = 'Good Morning!!!'
    elif hour < 16:
        msg = 'Good Afternoon!!!'
    elif hour < 20:
        msg = 'Good Evening!!!'
    elif hour <= 23:
        msg = 'Good Night!!!' 
    else:
        msg = 'Shut up and go to sleep!!!'
    my_dict = {'message': msg, 'timestamp': date, 'hour': hour, 'name': 'Srikar Madhavapeddy'}
    return render(request, 'testApp/index1.html', context=my_dict)