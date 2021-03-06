from django.shortcuts import render
from django.shortcuts import HttpResponse
from login import models

# Create your views here.

# user_list = []
#第一个参数必须是request,这是默认规定，request参数封装了用户请求的所有内容
#index()视图函数处理用户请求（编写业务逻辑）
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        # temp = {'user':username, 'pwd':password}
        # user_list.append(temp)
        models.userInfo.objects.create(user = username, pwd = password)
    user_list = models.userInfo.objects.all()
    # return HttpResponse('Hello World!')
    return render(request, 'login/index.html', {'data': user_list})

def index2(request):
    return HttpResponse('当前的命名空间是%s'% request.resolver_match.namespace)

def detail(request):
    if request.resolver_match.namespace == 'author':
        return HttpResponse('这里是作者的页面')
    elif request.resolver_match.namespace == 'publisher':
        return HttpResponse('这里是出版商的页面！')
    else:
        return HttpResponse('去玩儿把！')

