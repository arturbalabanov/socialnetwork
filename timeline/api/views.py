from rest_framework.generics import ListCreateAPIView

from timeline.api.permissions import IsAuthorOrReadOnly
from timeline.api.serializers import PostSerializer
from timeline.models import Post


class PostListCreate(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
