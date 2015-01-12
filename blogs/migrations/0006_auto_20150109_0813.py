# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20150109_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='downnum',
            field=models.IntegerField(verbose_name='\u5dee\u8bc4'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='upnum',
            field=models.IntegerField(verbose_name='\u597d\u8bc4'),
            preserve_default=True,
        ),
    ]
