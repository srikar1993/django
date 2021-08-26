from django.shortcuts import render
from django.views.generic import View, TemplateView
from  django.http import HttpResponse

# Create your views here.

# class HelloWorldView(View):
#     def get(self, request):
#         return HttpResponse('<h1>Response from class based views</h1>')

# class HelloWorldTemplateView(TemplateView):
#     template_name = 'testApp/index.html'

class ContextTemplateView(TemplateView):
    template_name = 'testApp/res.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Srikar'
        context['age'] = 27
        context['subject'] = 'Python'
        return context

