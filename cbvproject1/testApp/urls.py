from testApp import views
from django.urls import path

urlpatterns = [
    # path('', views.HelloWorldView.as_view()),
    # path('', views.HelloWorldTemplateView.as_view()),
    path('', views.ContextTemplateView.as_view()),
]