from blog.models import Blog, Category, Tag
from django import template
register = template.Library()


@register.simple_tag
def get_new_blog():
    return Blog.objects.all().order_by('-create_time')[:5]


@register.simple_tag
def archives():
    return Blog.objects.dates('create_time', 'month', order='DESC')


@register.simple_tag
def get_category():
    return Category.objects.all()


@register.simple_tag
def get_tag():
    return Tag.objects.all()