from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    # return HttpResponse("hello !")
    return render(request, "login.html")


# 登录操作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        # if username == 'admin' and password == '1':
        if user is not None:
            auth.login(request, user)
            # res.set_cookie('user', username, 3600)  # 添加浏览器的cookie
            request.session["user"] = username  # session 信息记录到浏览器
            # return HttpResponse("恭喜您，登录成功 ！")
            res = HttpResponseRedirect('/event_manage/')
            return res
        else:
            return render(request, 'login.html', {'error': '用户名或者密码错误！'})
    else:
        return render(request, 'login.html', {'error': '非法请求！'})


# 登录成功的页面
@login_required
def event_manage(request):
    # username = request.COOKIES.get('user','')  # cookies
    username = request.session.get('uesr''')  # session
    return render(request, "event_manage.html",{'user':username})
