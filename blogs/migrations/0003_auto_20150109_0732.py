# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20150109_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blogboby',
            field=models.TextField(verbose_name='\u6b63\u6587'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.DateTimeField(verbose_name='\u65f6\u95f4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=150, verbose_name='\u6807\u9898'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='address',
            field=models.CharField(max_length=30, verbose_name='IP'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='\u8bc4\u8bba'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(verbose_name='\u8bc4\u8bba\u65f6\u95f4'),
            preserve_default=True,
        ),
    ]
