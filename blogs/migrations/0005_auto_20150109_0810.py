# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20150109_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='downnum',
            field=models.IntegerField(verbose_name='\u8d2c'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='upnum',
            field=models.IntegerField(verbose_name='\u8d5e'),
            preserve_default=True,
        ),
    ]
