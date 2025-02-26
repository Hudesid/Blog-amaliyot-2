from django.urls import path
from . import views


urlpatterns = [
    path('tags/', views.TagListAPIView.as_view(), name='tag-list'),
    path('tags/posts/', views.PostOfTagListAPIView.as_view(), name="posts-of-tag")
]