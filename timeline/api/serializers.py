from rest_framework import serializers

from timeline.models import Post, PostComment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'number_of_likes', 'created')


class PostCommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post_id = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = PostComment
        fields = ('id', 'post_id', 'text', 'author', 'number_of_likes', 'created')
