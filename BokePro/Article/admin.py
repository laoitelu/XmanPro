# -*-coding:utf8-*-
from django.contrib import admin
from models import Post


# Register your models here.

@admin.register(Post)
class SitePost(admin.ModelAdmin):
    list_display = ("title", "post_type", "author", "c_time")
