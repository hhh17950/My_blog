from django.contrib.syndication.views import Feed
from .models import Blog


class AllPostsRssFeed(Feed):
    title = '橙子于渔个人博客'
    link = "/"
    description = "简易的个人博客"

    def items(self):
        return Blog.objects.all()

    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return str(item.id)

