from rest_framework import serializers

from timeline.models import Post, PostComment


class PostCommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), source='post')

    class Meta:
        model = PostComment
        fields = ('id', 'post_id', 'text', 'author', 'number_of_likes', 'created')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = PostCommentSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'number_of_likes', 'created', 'comments')

