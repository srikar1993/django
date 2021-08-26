from django.shortcuts import render
from django.http import request
from . import forms

# Create your views here.
def feedback_view(request):    
    if request.method == 'GET':
        form = forms.FeedBackForm()
        return render(request, 'testApp/index.html', {'form': form})

    if request.method == 'POST':
        form = forms.FeedBackForm(request.POST)
        if form.is_valid():
            my_dict = {'form': form, 'name': form.cleaned_data['name'], 'rollNo': form.cleaned_data['rollNo'], 'email': form.cleaned_data['email'], 'feedback': form.cleaned_data['feedback']}
            return render(request, 'testApp/register.html', context=my_dict)
    return render(request, 'testApp/index.html', {'form': form})

