from django.shortcuts import render
from testApp import forms

# Create your views here.

def student_view(request):
    if request.method == 'GET':
        form = forms.RegistrationForm()
        return render(request, 'testApp/index.html', {'form': form})
    
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            my_dict = {'form': form, 'name': form.cleaned_data['name'], 'marks': form.cleaned_data['marks']}
            # return render(request, 'testApp/congrats.html', context=my_dict)
            return render(request, 'testApp/index.html', {'form': form})