# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor_uploader.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('author', models.CharField(max_length=50, verbose_name='\u4f5c\u8005')),
                ('Guide_reading', models.TextField(max_length=300, verbose_name='\u6587\u7ae0\u5bfc\u8bfb')),
                ('c_time', models.DateTimeField(default=datetime.datetime(2018, 6, 21, 3, 5, 33, 343000, tzinfo=utc), verbose_name='\u53d1\u5e03\u65e5\u671f')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u5185\u5bb9')),
            ],
            options={
                'verbose_name': '\u535a\u5ba2',
                'verbose_name_plural': '\u535a\u5ba2\u7ba1\u7406',
            },
        ),
    ]
