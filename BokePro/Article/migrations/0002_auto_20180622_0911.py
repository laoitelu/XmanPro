# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.IntegerField(default=0, verbose_name='\u7c7b\u578b', db_column='\u6587\u7ae0\u7c7b\u578b', choices=[(0, b'PYTHON'), (1, b'SELENIUM'), (2, b'DJANGO')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='c_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 22, 1, 11, 43, 570000, tzinfo=utc), verbose_name='\u53d1\u5e03\u65e5\u671f'),
        ),
    ]
