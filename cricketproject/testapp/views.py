from django.shortcuts import render
from testapp.models import Cricket
from testapp import forms

# Create your views here.

def welcome_view(request):
    return render(request, 'testapp/welcome.html')

def addmatch_view(request):
    if request.method == 'GET':
        form = forms.CricketForm()
        return render(request, 'testapp/addmatch.html', {'form': form})
    
    if request.method == 'POST':
        form = forms.CricketForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return render(request, 'testapp/welcome.html')

def matcheslist_view(request):
    matches_list = Cricket.objects.all()
    return render(request, 'testapp/matcheslist.html', {'matches_list': matches_list})