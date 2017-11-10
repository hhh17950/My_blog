from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from blog.models import Blog
from .forms import UserCommentForm
from comment.models import UserComment
# Create your views here.


class CommentView(View):
    def post(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('users:login'))
        form = UserCommentForm(request.POST)
        if form.is_valid():
            user_comment = UserComment()
            user_comment.user = request.user
            user_comment.blog = blog
            user_comment.comment = form.cleaned_data['comment']
            user_comment.save()
            return HttpResponseRedirect(reverse('blog:detail', args=[blog_id]))
        else:
            return render(request, 'blog_detail.html', {
                'form': form
            })
