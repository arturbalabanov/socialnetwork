from django.conf.urls import url
from rest_framework import routers

from timeline.api.viewsets import PostViewSet, PostCommentViewSet

# urlpatterns = [
#     url(r'posts/$', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='create_post'),
#     url(r'posts/like/$', PostViewSet.as_view({'post': 'like'}), name='like_post'),
#     # url(r'post/like/$', LikeTimelinePostView.as_view(), name='like_post'),
# ]

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'post_comments', PostCommentViewSet)
urlpatterns = router.urls
