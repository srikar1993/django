from django.urls import path
from testApp import views

urlpatterns = [
    path('', views.Home.as_view()),
    path('home/', views.Home.as_view()),
    path('retrieve/', views.BookListView.as_view()),
    path('single/<pk>', views.BookDetailView.as_view()),
]