from django.urls import path
from testApp import views

urlpatterns = [
    path('', views.home_view),
    path('home/', views.home_view),
]
