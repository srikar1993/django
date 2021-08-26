from django.urls import path, include
from testApp import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('home/', views.HomeView.as_view()),
    path('retrieve/', views.InnovationListView.as_view(), name='retrieve'),
    path('single/<int:pk>/', views.InnovationDetailView.as_view(), name='single'),
    path('create/', views.InnovationCreateView.as_view()),
    path('update/<int:pk>/', views.InnovationUpdateView.as_view()),
    path('delete/<int:pk>/', views.InnovationDeleteView.as_view()),
]
