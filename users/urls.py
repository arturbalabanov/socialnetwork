from django.conf.urls import url

from users.views import *

urlpatterns = [
    url(r'login/$', LoginView.as_view(), name='login'),
    url(r'logout/$', LogoutView.as_view(), name='logout'),
    url(r'register/$', RegisterView.as_view(), name='register'),
    url(r'profile/(?P<slug>[\w.@+-]+)/$', ProfileView.as_view(), name='profile'),
    url(r'get-posts/(?P<username>[\w.@+-]+)/$', get_user_posts, name='get-posts'),
    url(r'friend/$', ToggleFriendshipView.as_view(), name='toggle_friendship'),
    url(r'search$', SearchView.as_view(), name='search_results'),
]
