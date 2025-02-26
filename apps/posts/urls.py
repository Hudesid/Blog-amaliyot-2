from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.PostListCreateAPIView.as_view(), name='posts-list'),
    path('post/<int:pk>/', views.PostRetrieveAPIView.as_view(), name='post-detail'),
    path('my/post/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='my-post-detail')
]