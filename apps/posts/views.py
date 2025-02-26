from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PostSerializer, Post
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import PostLimitOffsetPagination


class AuthorValidate(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PostLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'author', 'categories', 'tags']
    ordering_fields = ['author', 'categories', 'tags', 'status', 'created_at', 'updated_at']


class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, AuthorValidate]