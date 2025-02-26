from django.urls import path
from . import views


urlpatterns = [
    path('posts/comments/', views.CommentCreateListAPIView.as_view(), name='posts-comments')
]