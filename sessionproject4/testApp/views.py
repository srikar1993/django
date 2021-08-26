from django.shortcuts import render
from testApp import forms

# Create your views here.

def add_item_view(request):
    form = forms.AddItemsForm()
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        # request.session['name'] = name
        # request.session['quantity'] = quantity
        request.session[name] = quantity
    return render(request, 'testApp/additems.html', {'form': form})

def display_items_view(request):
    return render(request, 'testApp/displayitems.html')

