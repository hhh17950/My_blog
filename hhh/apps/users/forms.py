from django import forms
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='用户账号')
    password = forms.CharField(required=True, min_length=6, label='密码')


class RegosterForm(forms.Form):
    username = forms.CharField(required=True, label='用户名')
    email = forms.EmailField(required=True, label='邮箱名')
    pass_word_1 = forms.CharField(required=True, min_length=6, label='密码')
    pass_word_2 = forms.CharField(required=True, min_length=6, label='请确认密码')
