from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView
from testApp.models import Book

# Create your views here.

class Home(TemplateView):
    template_name = 'testApp/home.html'

class BookListView(ListView):
    model = Book
    # Default Template file ===> book_list.html (modelName_list.html)
    # Default Context ===> book_list
    
    # template_name = 'testApp/retrieve.html'
    # context_object_name = 'list_of_books'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['records'] = self.get_queryset().count()
    #     return context

class BookDetailView(DetailView):
    model = Book
    # template_name = 'testApp/single.html'
    # Default template name ===> book_detail.html
    # Default context ===> book or object