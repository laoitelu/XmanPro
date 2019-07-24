# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=30, verbose_name='\u5bc6\u7801')),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='\u53f7\u7801')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='\u90ae\u7bb1')),
                ('c_time', models.DateTimeField(default=datetime.datetime(2018, 6, 21, 2, 43, 32, 919000, tzinfo=utc), verbose_name='\u521b\u952e\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u7ba1\u7406',
                'verbose_name_plural': '\u7528\u6237\u5217\u8868',
            },
        ),
    ]
