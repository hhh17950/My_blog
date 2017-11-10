from django.shortcuts import render
from django.views.generic.base import View
from .forms import LoginForm, RegosterForm
from users.models import UserProfile, EmailCode
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
import re
from utils.email_send import send_email_type
# Create your views here.


# 自定义用户鉴定的方法


class CostomBankend(ModelBackend):
    """自定义鉴定类型"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            pass_word = form.cleaned_data['password']
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                else:
                    return render(request, 'login.html', {
                        'form': form,
                        'msg': '用户未激活'
                    })
                return HttpResponseRedirect(reverse('index'))
            else:
                msg = '用户名或密码错误'
                return render(request, 'login.html', {
                    'form': form,
                    'msg': msg,
                })
        else:
            return render(request, 'login.html', {
                'form': form,
            })


class ActiveView(View):
    def get(self, request, active_code):
        all_code = EmailCode.objects.filter(code=active_code)
        if all_code:
            for code in all_code:
                email = code.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        return HttpResponseRedirect(reverse('users:login'))


class RegisterView(View):
    def get(self, request):
        form = RegosterForm()
        return render(request, 'register.html', {
            'form': form,
        })

    def post(self, request):
        form = RegosterForm(request.POST)
        login_form = LoginForm()
        if form.is_valid():
            user = UserProfile()
            user_name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            pwd_1 = form.cleaned_data['pass_word_1']
            pwd_2 = form.cleaned_data['pass_word_2']
            s = re.match('(?!^\d+$)(?!^[a-zA-Z]+$)[0-9a-zA-Z]{6,23}', user_name)
            if s is not None:
                if UserProfile.objects.filter(username=user_name):
                    return render(request, 'register.html', {
                        'form': form,
                        'msg': '该账户以存在'
                    })
                if pwd_1 != pwd_2:
                    return render(request, 'register.html', {
                        'form': form,
                        'msg': '密码输入不一致'
                    })
                user.username = user_name
                user.email = email
                user.password = make_password(pwd_1)
                user.is_active = False
                user.save()
                send_email_type(email, 'register')
                return HttpResponseRedirect(reverse('users:login'))
            else:
                return render(request, 'register.html', {
                    'form': form,
                    'msg': '请输入正确的用户账号，只能由字母与数字组成, 且最小长度为6位'
                })
