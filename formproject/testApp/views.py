from django.shortcuts import render
from django.http import request
from . import forms

# Create your views here.

def studentRegistrationView(request):
    if request.method == 'GET':
        form = forms.StudentRegistration()
        return render(request, 'testApp/register.html', {'form': form})

    if request.method == 'POST':

        form = forms.StudentRegistration(request.POST)
        if form.is_valid():
            my_dict = {'form': form, 'name': form.cleaned_data['name'], 'marks': form.cleaned_data['marks'], 'email': form.cleaned_data['email'], 'feedback': form.cleaned_data['feedback']}
            return render(request, 'testApp/test.html', context = my_dict)