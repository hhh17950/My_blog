from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=15, verbose_name='昵称', null=True, blank=True)
    birday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(choices=(('male', '男'), ('female', '女')),
                              default='female', max_length=6, verbose_name='性别')
    address = models.CharField(max_length=100, default='', verbose_name='地址', null=True, blank=True)
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号码')
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png",
                              max_length=100, verbose_name='用户头像')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailCode(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(choices=(('register', '注册'), ('forget', '找回密码'), ('update_email', '修改邮箱')),
                                 max_length=12, verbose_name='验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name
    # 定义返回的形式

    def __str__(self):
        return "{0}({1})".format(self.code, self.email)