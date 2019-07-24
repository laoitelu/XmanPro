# -*-coding:utf8-*-
from django.db import models
import django.utils.timezone as timezone


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30, verbose_name=u"用户名")
    password = models.CharField(max_length=30, verbose_name=u"密码")
    phone = models.CharField(max_length=20, null=True, verbose_name=u"号码")
    email = models.EmailField(null=True, verbose_name=u"邮箱")
    c_time = models.DateTimeField(default=timezone.now(), verbose_name=u"创键时间")

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = u"用户"
        verbose_name_plural = u"用户管理"
