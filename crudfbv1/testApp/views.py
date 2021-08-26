from django.shortcuts import render, redirect
from testApp.models import Employee
from testApp.forms import EmployeeForms

# Create your views here.

def home_view(request):
    return render(request, 'testApp/home.html')

def create_view(request):
    if request.method == 'GET':
        form = EmployeeForms()
        return render(request, 'testApp/create.html', {'form': form})
    if request.method == 'POST':
        form = EmployeeForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/retrieve')

def retrieve_view(request):
    employee_list = Employee.objects.all()
    # employee_count = Employee.objects.all().count()
    employee_count = len(list(employee_list))
    return render(request, 'testApp/retrieve.html', {'employee_list': employee_list, 'records': employee_count})

def update_view(request, id):
    employee = Employee.objects.get(id = id)
    if request.method == 'GET':
        return render(request, 'testApp/update.html', {'employee': employee})
    if request.method == 'POST':
        form = EmployeeForms(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/retrieve')

def delete_view(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/retrieve')
