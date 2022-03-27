from django.conf.urls import url
from . import views

urlpatterns = [
    path('index/', views.index),
]