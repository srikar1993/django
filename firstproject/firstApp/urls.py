from django.urls import path
from firstApp import views

urlpatterns = [
    path('hello/', views.welcome),
    path('home/', views.home),
]