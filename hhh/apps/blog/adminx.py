import xadmin
from .models import Category, Tag, Blog


class CategoryAdmin(object):
    search_fields = ['name']


class TagAdmin(object):
    search_fields = ['name']


class BlogAdmin(object):
    list_display = ['category', 'tag', 'title', 'author', 'excerpt', 'click_nums', 'create_time']
    search_fields = ['category', 'tag', 'title', 'author', 'excerpt', 'click_nums']
    list_filter = ['category__name', 'tag', 'title', 'author__username', 'excerpt', 'click_nums', 'create_time']


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Blog, BlogAdmin)