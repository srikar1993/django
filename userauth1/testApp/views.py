from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testApp import forms
from django.http import HttpResponseRedirect

# Create your views here.

def home_view(request):
    return render(request, 'testApp/home.html')

@login_required
def java_view(request):
    return render(request, 'testApp/java.html')

@login_required
def python_view(request):
    return render(request, 'testApp/python.html')

@login_required
def results_view(request):
    return render(request, 'testApp/results.html')

def signup_view(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            # form.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'testApp/signup.html', {'form': form})

def thank_you_view(request):
    return render(request, 'testApp/thankyou.html')