from rest_framework.generics import ListAPIView
from .serializers import Tag, TagSerializer
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from apps.posts.views import PostSerializer, PostLimitOffsetPagination, OrderingFilter, Post


class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['name']


class PostOfTagListAPIView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PostLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'author', 'categories', 'tags']
    ordering_fields = ['author', 'categories', 'tags', 'status', 'created_at', 'updated_at']


    def get_queryset(self):
        return Post.objects.filter(tags__id=self.kwargs['tag_id'])

