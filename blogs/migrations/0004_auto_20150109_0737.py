# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20150109_0732'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u535a\u5ba2'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u5206\u7c7b', 'verbose_name_plural': '\u5206\u7c7b\u4e2d\u5fc3'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '\u8bc4\u8bba', 'verbose_name_plural': '\u8bc4\u8bba'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='\u5206\u7c7b\u540d\u79f0'),
            preserve_default=True,
        ),
    ]
