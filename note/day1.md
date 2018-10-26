### 4-4
1. 使用Python2 安装virtualenv,使用虚拟化环境创建项目
2. 安装mysql，会报错，访问https://www.lfd.uci.edu/~gohlke/pythonlibs/ 下载mysql驱动
同时设置setting.py
~~~
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'mxonline',
        'USER': 'root',
        'PASSWORD': '',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
~~~
### 4-5
1. 现有user表不满足现有需求，所以创建users APP
2. 设计users model.py
~~~
from django.contrib.auth.models import AbstractUser #引入系统user表 AbstractUser
from django.db import models


# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    birday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(max_length=5, choices=(("male", u"男"), ("female", u"女")), default="female")
    address = models.CharField(max_length=100, default=u"")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
~~~
3. setting.py 注册APP，同时设置AUTH_USER_MODEL = "users.UserProfile" 重写用户模型
~~~
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
]
AUTH_USER_MODEL = "users.UserProfile"
~~~
4. 安装 pillow  pip2 install pillow

### 4-6
1. 增加邮箱验证码model及banner model
~~~

~~~