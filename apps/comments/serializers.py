from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'created_at', 'updated_at', 'content', 'parent_comment', 'comments')


    def get_comments(self, obj):
        return CommentSerializer(obj.sub_comment.all(), many=True).data

    def create(self, validated_data):
        comment = Comment.objects.create(
            author=self.context['request'].user
            **validated_data
        )
        comment.save()
        return comment

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.author = self.context['request'].user
        instance.save()
        return instance