from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'author', 'created_at', 'updated_at')
    list_filter = ('status', 'author__username', 'created_at', 'updated_at')
    search_fields = ('id', 'title', 'author__username')