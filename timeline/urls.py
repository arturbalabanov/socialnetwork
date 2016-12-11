from django.conf.urls import url

from timeline.api.views import PostListCreate
from timeline.views import *

urlpatterns = [
    # url(r'post/create/$', MakeTimelinePostView.as_view(), name='create_post'),
    url(r'post/create/$', PostListCreate.as_view(), name='create_post'),
    url(r'post/like/$', LikeTimelinePostView.as_view(), name='like_post'),
]
