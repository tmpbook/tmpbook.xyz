# coding:utf8
__author__ = 'kevin gao'

from django.conf.urls import url
from .views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]
