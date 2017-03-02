from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response

from timeline.api.permissions import PostPermission, PostCommentPermission
from timeline.api.serializers import PostSerializer, PostCommentSerializer
from timeline.models import Post, PostComment
from users.api.serializers import UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (PostPermission,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @list_route(methods=['post'])
    def like(self, serializer):
        post = get_object_or_404(self.queryset, pk=serializer.data.get('id'))
        post.like(self.request.user)
        response_serializer = PostSerializer(post)  # FIXME: maybe serializer_class(post)?
        return Response(response_serializer.data)

    @detail_route(url_path='get-likes')
    def get_likes(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        likes = post.likes.all()
        response_serializer = UserSerializer(likes, many=True)
        return Response(response_serializer.data)


class PostCommentViewSet(viewsets.ModelViewSet):
    serializer_class = PostCommentSerializer
    queryset = PostComment.objects.all()
    permission_classes = (PostCommentPermission,)

    def perform_create(self, serializer):
        post = get_object_or_404(Post.objectsj.all(), pk=serializer.data.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    @list_route(methods=['post'])
    def like(self, serializer):
        comment = get_object_or_404(self.queryset, pk=serializer.data.get('id'))
        comment.like(self.request.user)
        response_serializer = PostCommentSerializer(comment)
        return Response(response_serializer.data)

    @detail_route(url_path='get-likes')
    def get_likes(self, request, pk=None):
        comment = get_object_or_404(self.queryset, pk=pk)
        likes = comment.likes.all()
        response_serializer = UserSerializer(likes, many=True)
        return Response(response_serializer.data)

