from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index/', views.index2, name = 'index'),
    path('detail/', views.detail, name = 'detail'),
]