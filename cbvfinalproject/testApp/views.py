from django.shortcuts import render
from testApp .models import Innovation
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class HomeView(TemplateView):
    template_name = 'testApp/home.html'

class InnovationListView(ListView):
    model = Innovation

class InnovationDetailView(DetailView):
    model = Innovation

class InnovationCreateView(CreateView):
    model = Innovation
    fields = '__all__'

class InnovationUpdateView(UpdateView):
    model = Innovation
    fields = '__all__'

class InnovationDeleteView(DeleteView):
    model = Innovation
    success_url = reverse_lazy('retrieve')
