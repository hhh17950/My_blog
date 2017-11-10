from django.shortcuts import render
from .models import Blog, Tag
from pure_pagination import Paginator, PageNotAnInteger
import markdown
from comment.forms import UserCommentForm
from comment.models import UserComment
from django.views.generic.base import View
from django.db.models import Q
# Create your views here.


class IndexView(View):
    def get(self, request):
        blog_lists = Blog.objects.all().order_by('create_time')
        counts = blog_lists.count()
        name = request.GET.get('tag', '')
        tag = Tag.objects.filter(name=name)
        q = request.GET.get('q', '')
        if q:
            blog_lists = blog_lists.filter(Q(title__icontains=q) | Q(body__icontains=q))
        if tag:
            blog_lists = blog_lists.filter(tag=tag)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(blog_lists, 3, request=request)
        blogs = p.page(page)
        return render(request, 'index.html', {
            'blog_lists': blogs,
            'counts': counts,
        })


def detail(request, blog_id):
    blog_lists = Blog.objects.all().order_by('create_time')
    counts = blog_lists.count()
    blog = Blog.objects.get(id=blog_id)
    blog.click_nums += 1
    blog.save()
    blog.save()
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    blog.body = md.convert(blog.body)
    blog.toc = md.toc
    form = UserCommentForm()
    all_comment = UserComment.objects.filter(blog_id=blog_id)
    return render(request, 'blog_detail.html', {
        'blog': blog,
        'form': form,
        'all_comment': all_comment,
        'counts': counts
    })


def archives(request, year, month):
    blog_list = Blog.objects.filter(create_time__year=year, create_time__month=month,).order_by('-create_time')
    return render(request, 'blog_archives.html', {
        'blog_list': blog_list,
    })


def category(request, category_id):
    blog_list = Blog.objects.filter(id=category_id).order_by('-create_time')
    return render(request, 'blog_category.html', {
        'blog_list': blog_list,
    })