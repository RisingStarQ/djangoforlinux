from django.shortcuts import render
from django.shortcuts import HttpResponse
from login import models

# Create your views here.

# user_list = []
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        # temp = {'user':username, 'pwd':password}
        # user_list.append(temp)
        models.userInfo.objects.create(user = username, pwd = password)
    user_list = models.userInfo.objects.all()
    return render(request, 'index.html', {'data': user_list})