from django.db import models
from users.models import UserProfile
from blog.models import Blog
from datetime import datetime
# Create your models here.


class UserComment(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    blog = models.ForeignKey(Blog, verbose_name='博客')
    comment = models.CharField(max_length=200, verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '博客评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comment[:20]
