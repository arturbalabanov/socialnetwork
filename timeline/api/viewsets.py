from rest_framework import viewsets

from timeline.api.permissions import IsAuthorOrReadOnly
from timeline.api.serializers import PostSerializer
from timeline.models import Post


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
