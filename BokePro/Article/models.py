# -*-coding:utf8-*-
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import django.utils.timezone as timezone


# Create your models here.

class Post(models.Model):
    Type = ((0, "Python"), (1, "Selenium"), (2, "Django"),)
    title = models.CharField(max_length=100, verbose_name=u"标题")
    post_type = models.IntegerField(choices=Type, default=0, verbose_name=u"类型", db_column=u"文章类型")
    author = models.CharField(max_length=50, verbose_name=u"作者")
    Guide_reading = models.TextField(max_length=300, verbose_name=u"文章导读")
    c_time = models.DateTimeField(default=timezone.now(), verbose_name=u"发布日期")
    content = RichTextUploadingField(verbose_name=u"内容")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"博客"
        verbose_name_plural = u"博客管理"
