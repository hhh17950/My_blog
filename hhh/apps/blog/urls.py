from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^detail/(?P<blog_id>\d+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'category/(?P<category_id>\d+)/$', views.category, name='category'),
]
