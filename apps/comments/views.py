from rest_framework.generics import ListCreateAPIView
from .serializers import Comment, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter


class CommentCreateListAPIView(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['author']
    ordering_fields = ['author', 'created_at', 'updated_at']
    ordering = ['author']

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        if post_id:
            return Comment.objects.filter(post__id=post_id)
        return Comment.objects.all()









