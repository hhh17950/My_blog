from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^blog_comment/(?P<blog_id>\d+)/$', views.CommentView.as_view(), name='blog_comment'),
]