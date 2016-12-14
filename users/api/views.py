from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from timeline.api.serializers import PostSerializer
from users.models import UserProfile


@api_view(['GET'])
def get_posts(request, username):
    user = get_object_or_404(UserProfile, username=username)
    posts = user.timeline_posts.all()
    post_serializer = PostSerializer(posts, many=True)

    return Response(post_serializer.data, status=status.HTTP_200_OK)

