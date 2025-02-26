from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'posts_count')


    def get_posts_count(self, obj):
        return obj.posts.count()