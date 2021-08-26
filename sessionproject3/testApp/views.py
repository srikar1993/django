from django.shortcuts import render
from testApp import forms

# Create your views here.

def name_view(request):
    form = forms.NameForm()
    return render(request, 'testApp/name.html', {'form': form})

def age_view(request):
    form = forms.AgeForm()
    name = request.GET['name']
    request.session['name'] = name
    return render(request, 'testApp/age.html', {'form': form, 'name': name})

def gf_view(request):
    form = forms.GfForm()
    age = request.GET['age']
    request.session['age'] = age
    name = request.session.get('name')
    return render(request, 'testApp/gf.html', {'form': form, 'name': name})

def results_view(request):
    gf = request.GET['gf']
    request.session['gf'] = gf
    return render(request, 'testApp/results.html')