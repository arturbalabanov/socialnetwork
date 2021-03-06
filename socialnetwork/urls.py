from django.conf.urls import url, include
from django.contrib import admin

from home.views import IndexView
from users import urls as users_urls
from timeline import urls as timeline_urls

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^users/', include(users_urls, namespace='users')),
    url(r'^timeline/', include(timeline_urls, namespace='timeline')),
    url(r'^admin/', admin.site.urls),
]
