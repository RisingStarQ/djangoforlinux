"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from argparse import Namespace
from django.contrib import admin
from django.urls import include, path
# from login import views

#path('index/', views.index) 路由转发用户请求到views.index视图函数
urlpatterns = [
	path('polls/', include('polls.urls')),
	path('index/', include('login.urls')),
    path('admin/', admin.site.urls),
    path('author/',include('login.urls', namespace = 'author')),
    path('publisher/', include('login.urls', namespace = 'publisher')),
]