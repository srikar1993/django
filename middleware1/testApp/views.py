from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# class HomeView(TemplateView):
#     print('This line is printed by Class Based View while processing the request...')
#     template_name = 'testApp/home.html'

def home_view(request):
    print('This line is printed by Function Based View while processing the request...')
    return render(request, 'testApp/home.html')
