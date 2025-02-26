from rest_framework import serializers
from .models import Post
from apps.authors.serializers import UserSerializer
from apps.categories.serializers import CategorySerializer
from apps.comments.serializers import CommentSerializer
from apps.tags.serializers import TagSerializer


class PostSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'created_at', 'updated_at', 'author', 'categories', 'tags', 'content', 'status')


    def get_comments_count(self, obj):
        return obj.comments.count()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = UserSerializer(instance.author).data
        representation['categories'] = CategorySerializer(instance.categories, many=True).data
        representation['comments'] = CommentSerializer(instance.comments, many=True).data
        representation['tags'] = TagSerializer(instance.tags, many=True).data
        return representation

    def create(self, validated_data):
        post = Post.objects.create(
            author=self.context['request'].user
            **validated_data
        )
        return post

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.author = self.context['request'].user
        instance.save()
        return instance