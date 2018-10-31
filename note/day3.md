### 第六章
1. 采用邮箱及用户名验证方式

#### setting.py 添加
~~~
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)
~~~
#### users.views 添加
~~~
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
class CustomBackend(ModelBackend):

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))  # Q代表或的关系
            if user.check_password(password):
                return user
        except Exception as e:
            return None
~~~
2. views 使用类编写
from django.views.generic.base import View

~~~
class LoginView(View):

    def get(self, request):
        return render(request, "login.html", {})

urls 修改
from users.views import LoginView

url(r'^login/$', views.LoginView.as_view(), name="login"),
~~~

3. 用户名密码使用form判断
login.html
~~~
 <div class="form-group marb20 {% if login_form.errors.username %}errorput{% endif %}">

    <label>用&nbsp;户&nbsp;名</label>
    <input name="username" id="account_l" type="text" placeholder="手机号/邮箱" />
 </div>
 {% if login_form.errors.username %}errorput{% endif %} 用法是如果用户名错误,则显示红色框框 login_form 取的是view里的
 ~~~