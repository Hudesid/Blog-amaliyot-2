from django.db import models
from django.contrib.auth import settings


class Comment(models.Model):
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey("self", on_delete=models.CASCADE, related_name='sub_comments', blank=True, null=True)