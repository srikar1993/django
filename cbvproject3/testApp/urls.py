from django.urls import path
from testApp import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('home/', views.HomeView.as_view()),
    path('retrieve/', views.CompanyListView.as_view(), name='retrieve'),
    path('single/<int:pk>/', views.CompanyDetailView.as_view(), name='single'),
    path('create/', views.CompanyCreateView.as_view()),
    path('update/<int:pk>/', views.CompanyUpdateView.as_view()),
    path('delete/<int:pk>/', views.CompanyDeleteView.as_view()),
]
