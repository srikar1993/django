from django.shortcuts import render
from testApp.models import Employee
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q, Avg, Sum, Min, Max, Count

# Create your views here.

class EmpHomeView(TemplateView):
    template_name = 'testApp/home.html'

class EmpListView(ListView):
    model = Employee

class EmpDetailView(DetailView):
    model = Employee

class EmpCreateView(CreateView):
    model = Employee
    fields = '__all__'

class EmpUpdateView(UpdateView):
    model = Employee
    fields = '__all__'

class EmpDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('retrieve')

def orm_view1(request):
    employees = Employee.objects.all()
    my_dict = {'employee_list': employees}
    return render(request, 'testApp/orm1.html', context=my_dict)

def orm_view2(request):
    employee = Employee.objects.get(eno=3060)
    my_dict = {'employee': employee}
    return render(request, 'testApp/orm2.html', context=my_dict)

def orm_view3(request):
    employees = Employee.objects.filter(esal__lte=20000)
    my_dict = {'employee_list': employees}
    return render(request, 'testApp/orm3.html', context=my_dict)

def orm_or_view(request):
    # OR - type1
    # employees = Employee.objects.filter(Q(esal__lt=20000) | Q(ename__startswith='m'))
    # OR - type2
    employees = Employee.objects.filter(esal__lt=20000) | Employee.objects.filter(ename__istartswith='M')
    my_dict = {'employee_list': employees}
    return render(request, 'testApp/orm_or.html', context=my_dict)

def orm_and_view(request):
    # And - type1
    # employees = Employee.objects.filter(Q(esal__lt=20000) & Q(ename__endswith='n'))
    # And - type2
    # employees = Employee.objects.filter(Q(esal__lt=20000), Q(ename__endswith='n'))
    # And - type3
    employees = Employee.objects.filter(esal__lt=20000) & Employee.objects.filter(ename__endswith='n')
    my_dict = {'employee_list': employees}
    return render(request, 'testApp/orm_and.html', context=my_dict)

def orm_union(request):
    emp1 = Employee.objects.filter(esal__range=(10000,20000))
    emp2 = Employee.objects.filter(Q(ename__startswith='M') | Q(ename__endswith='n'))
    employees = emp1.union(emp2)
    my_dict = {'employee_list': employees}
    return render(request, 'testApp/orm_union.html', context=my_dict)

def orm_exclude(request):
    employee = Employee.objects.exclude(esal__gte=20000)
    my_dict = {'employee_list': employee}
    return render(request, 'testApp/orm_exclude.html', context=my_dict)

def orm_values_list(request):
    employee = Employee.objects.values_list('eno', 'ecity')
    my_dict = {'employee_list': employee}
    return render(request, 'testApp/orm_values_list.html', context=my_dict)

def orm_values(request):
    employee = Employee.objects.all().values('eno', 'ecity')
    my_dict = {'employee_list': employee}
    return render(request, 'testApp/orm_values.html', context=my_dict)

def orm_only(request):
    employee = Employee.objects.all().only('eno', 'ecity')
    my_dict = {'employee_list': employee}
    return render(request, 'testApp/orm_only.html', context=my_dict)

def orm_orderby(request):
    # Ascending order
    employee = Employee.objects.all().order_by('ename')
    # Descending order
    # employee = Employee.objects.all().order_by('-ename')
    my_dict = {'employee_list': employee}
    return render(request, 'testApp/orm_orderby.html', context=my_dict)

def orm_agg(request):
    sum1 = Employee.objects.all().aggregate(Sum('esal'))
    avg = Employee.objects.all().aggregate(Avg('esal'))
    max1 = Employee.objects.all().aggregate(Max('esal'))
    min1 = Employee.objects.all().aggregate(Min('esal'))
    count1 = Employee.objects.all().aggregate(Count('esal'))
    my_dict = {'sum':sum1, 'avg':avg, 'min':min1, 'max':max1, 'count':count1}
    return render(request, 'testApp/orm_agg.html', context=my_dict)