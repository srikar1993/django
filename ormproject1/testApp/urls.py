from django.urls import path
from testApp import views

urlpatterns = [
    path('', views.EmpHomeView.as_view()),
    path('home/', views.EmpHomeView.as_view(), name='home'),
    path('retrieve/', views.EmpListView.as_view(), name='retrieve'),
    path('single/<int:pk>/', views.EmpDetailView.as_view(), name='single'),
    path('create/', views.EmpCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.EmpUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.EmpDeleteView.as_view(), name='delete'),
    path('orm1/', views.orm_view1, name='orm1'),
    path('orm2/', views.orm_view2, name='orm2'),
    path('orm3/', views.orm_view3, name='orm3'),
    path('ormor/', views.orm_or_view, name='orm_or'),
    path('ormand/', views.orm_and_view, name='orm_and'),
    path('ormunion/', views.orm_union, name='orm_union'),
    path('ormexclude/', views.orm_exclude, name='orm_exclude'),
    path('ormvalueslist/', views.orm_values_list, name='orm_values_list'),
    path('ormvalues/', views.orm_values, name='orm_values'),
    path('ormonly/', views.orm_only, name='orm_only'),
    path('ormorderby/', views.orm_orderby, name='orm_orderby'),
    path('ormagg/', views.orm_agg, name='orm_agg'),

]