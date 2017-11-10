import xadmin
from .models import UserComment


class UserCommentAdmin(object):
    list_display = ['user', 'blog', 'comment', 'add_time']
    search_fields = ['user', 'blog', 'comment']
    list_filter = ['user__username', 'blog__title', 'comment', 'add_time']


xadmin.site.register(UserComment, UserCommentAdmin)
