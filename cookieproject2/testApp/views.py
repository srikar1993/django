from django.http import response
from django.shortcuts import render

# Create your views here.

def name_view(request):
    return render(request, 'testApp/name.html')

def age_view(request):
    name = request.GET['name']
    response = render(request, 'testApp/age.html', {'name': name})
    response.set_cookie('name', name)
    return response
    
def gf_view(request):
    age = request.GET['age']
    name = request.COOKIES.get('name')
    response = render(request, 'testApp/gf.html', {'name': name})
    response.set_cookie('age', age)
    return response

def results_view(request):
    gf = request.GET['gf']
    name = request.COOKIES.get('name')
    age = request.COOKIES.get('age')
    my_dict = {'name': name, 'age': age, 'gf': gf}
    response = render(request, 'testApp/results.html', context=my_dict)
    response.set_cookie('gf', gf)
    return response