## xadmin
###安装方式1:
pip install xadmin

###安装方式2:

1. 下载源码 https://github.com/sshwsfc/xadmin
2. 在项目目录下新建extra_apps 把下载下来的xadmin文件放入extra_apps下
3. 安装必要库
~~~
django>=1.9.0
django-crispy-forms>=1.6.0
django-import-export>=0.5.1
django-reversion>=2.0.0
django-formtools==1.0
future==0.15.2
httplib2==0.9.2
six==1.10.0
~~~
4. 把extra_apps目录设置为 source root
5. 然后在MxOnline2/settings里面添加
~~~
import sys
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))
~~~


6. 修改MxOnline2/urls
~~~
import xadmin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),

]
~~~
7. 在每个app下面添加adminx.py 文件, 比如user
~~~
# -*- coding: utf-8 -*-
import xadmin
from .models import EmailVerifyRecord, Banner, UserProfile
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True  # 设置主题


class GlobalSettings(object):
    site_title = "慕学后台管理系统"  # 头部
    site_footer = "慕学在线网"  # 底部
    menu_style = "accordion"  # 菜单折叠


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    # list_editable = ['code', 'email', 'send_type', 'send_time']
    # model_icon = 'fa fa-address-book-o'


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

~~~
8. 主题设置会有问题, 显示不全, 参考https://www.jianshu.com/p/8d4d958b8e82
9. 左边菜单栏会显示app名称, 修改app下面的apps.py 文件, 比如users.apps
~~~
class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = u"用户信息"  # 别名
~~~
然后修改users.__init__.py
~~~
default_app_config = "users.apps.UsersConfig"
~~~