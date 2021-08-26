from django.shortcuts import render
from django.views.generic.edit import DeleteView
from testApp.models import Company
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DetailView
from django.urls import reverse, reverse_lazy

# Create your views here.

class HomeView(TemplateView):
    template_name = 'testApp/home.html'

class CompanyListView(ListView):
    model = Company
    # Default html file ===> company_list.html
    # Default context ===> company_list

class CompanyDetailView(DetailView):
    model = Company
    # Default html file ===> company_detail.html
    # Default context ===> company or object

class CompanyCreateView(CreateView):
    model = Company
    fields = ('name', 'location', 'ceo')
    # Default html file ===> company_form.html

class CompanyUpdateView(UpdateView):
    model = Company
    fields = ('name', 'location', 'ceo')
    # Default html file ===> company_form.html ... Same as CreateView

class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('retrieve')
    # Default html file ===> company_confirm_delete.html ... This html file is recommended for security purposes.