from django.db import models
from users.models import UserProfile
from datetime import datetime
import markdown
from django.utils.html import strip_tags
# Create your models here.


class Category(models.Model):
    """博客的分类"""
    name = models.CharField(max_length=20, verbose_name='分类')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def post_count(self):
        return self.blog_set.count()


class Tag(models.Model):
    """标签"""
    name = models.CharField(max_length=20, verbose_name='标签')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Blog(models.Model):
    category = models.ForeignKey(Category, verbose_name='分类')
    author = models.ForeignKey(UserProfile, verbose_name='作者')
    tag = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    title = models.CharField(max_length=50, verbose_name='标题')
    excerpt = models.CharField(max_length=200, blank=True, null=True, verbose_name='摘要')
    body = models.TextField()
    click_nums = models.IntegerField(default=0, verbose_name='观看数')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='发表时间')
    edit_time = models.DateTimeField(verbose_name='修改时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

            # 调用父类的 save 方法将数据保存到数据库中
        super(Blog, self).save(*args, **kwargs)

    def blog_count(self):
        counts = self.usercomment_set.count()
        return counts
