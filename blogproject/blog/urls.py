from django.urls import path
from blog import views

urlpatterns = [
    # For FBV -> post_list_view
    path('', views.post_list_view, name='post_list'),
    path('home/', views.post_list_view, name='post_list'),
    path('tag/<slug:tag_slug>', views.post_list_view, name='post_list_by_tag_name'),
    # For CBV -> PostListView
    # path('', views.PostListView.as_view(), name='post_list'),
    # path('home/', views.PostListView.as_view(), name='post_list'),
    # path('(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/', views.post_detail_view, name='post_detail'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail_view, name='post_detail'),
    path('email/post/<int:id>/', views.mail_send_view, name='send_mail'),
]
