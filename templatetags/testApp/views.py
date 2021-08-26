from django.shortcuts import render
from testApp.models import Sports

# Create your views here.

def welcome_view(request):
    return render(request, 'testApp/home.html')

def sports_view(request):
    sports_list = Sports.objects.all()
    return render(request, 'testApp/sports.html', {'sports_list': sports_list})