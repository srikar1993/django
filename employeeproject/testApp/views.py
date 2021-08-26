from django.shortcuts import render
from testApp.models import Employee
from django.http import HttpResponse

# Create your views here.

def empview(request):
    emp_list = Employee.objects.all()
    my_dict = {'empList': emp_list}
    return render(request, 'testApp/index.html', context=my_dict)