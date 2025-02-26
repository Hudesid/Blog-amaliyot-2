from rest_framework import serializers
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ('id', 'name', 'created_at', 'updated_at', 'posts_count')


    def get_posts_count(self, obj):
        return obj.posts.count()