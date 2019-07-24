# -*-coding:utf8-*-
from django.contrib import admin
from models import User


# Register your models here.

@admin.register(User)
class SiteUserAdmin(admin.ModelAdmin):
    list_display = ("username", "phone", "email", "c_time")
    list_per_page = 20
    search_fields = ("username",)


admin.site.site_header = u"XlMan后台管理系统"
admin.site.site_title = u"XlMan后台管理系统"
