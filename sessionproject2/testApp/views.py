from django.http import response
from django.shortcuts import render

# Create your views here.

def name_view(request):
    return render(request, 'testApp/name.html')

def age_view(request):
    name = request.GET['name']
    response = render(request, 'testApp/age.html', {'name': name})
    request.session['name'] = name
    return response
    
def gf_view(request):
    age = request.GET['age']
    name = request.session.get('name')
    response = render(request, 'testApp/gf.html', {'name': name})
    request.session['age'] = age
    return response

def results_view(request):
    gf = request.GET['gf']
    name = request.session.get('name')
    age = request.session.get('age')
    my_dict = {'name': name, 'age': age, 'gf': gf}
    response = render(request, 'testApp/results.html', context=my_dict)
    request.session['gf'] = gf
    return response