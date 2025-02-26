from rest_framework.generics import ListAPIView
from .serializers import CategorySerializer, Category
from .paginations import CategoryLimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from apps.posts.serializers import PostSerializer, Post


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryLimitOffsetPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['name']


class PostsOfCategoryListAPIView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'author']
    ordering_fields = ['author', 'tags', 'status']

    def get_queryset(self):
        return Post.objects.filter(category__id=self.kwargs['category_id'])
