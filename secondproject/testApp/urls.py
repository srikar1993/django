from django.urls import path
from testApp import views

urlpatterns = [
    path('test/', views.dateinfo),
    path('tests/', views.greeting),
]