from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from timeline.api.permissions import PostPermission
from timeline.api.serializers import PostSerializer
from timeline.models import Post


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
