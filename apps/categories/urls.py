from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/posts/<int:pk>', views.PostsOfCategoryListAPIView.as_view(), name='posts-of-category')
]