#!-*- coding:utf-8 -*-

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from users.models import UserProfile
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm


# Create your views here.

class CustomBackend(ModelBackend):
    """
    邮箱和用户名都可以登录 在setting 添加
    AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',)
    """

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))  # Q代表或的关系
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):

    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            # print(user_name, pass_word)
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                # if user.is_active:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, "login.html", {"msg": u"用户名或密码错误"})  # {"msg": u"用户名或密码错误！"}
        else:
            return render(request, "login.html", {"login_form": login_form})
