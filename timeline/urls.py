from django.conf.urls import url

from timeline.api.viewsets import PostViewSet
from timeline.views import *

urlpatterns = [
    url(r'posts/$', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='create_post'),
    url(r'post/like/$', LikeTimelinePostView.as_view(), name='like_post'),
]
