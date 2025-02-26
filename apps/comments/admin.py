from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author__username', 'created_at', 'updated_at')
    list_filter = ('author__username', 'created_at', 'updated_at', 'post__title', 'id')
    search_fields = ('author__name', 'id', 'post__title')