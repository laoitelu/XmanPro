#  -*-coding:utf8-*-
from django.conf.urls import url
from views import *
urlpatterns = [
    url(r'^list/$', post)
]
