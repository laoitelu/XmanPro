# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='c_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 21, 2, 44, 18, 309000, tzinfo=utc), verbose_name='\u521b\u952e\u65f6\u95f4'),
        ),
    ]
