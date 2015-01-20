# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcrawler', '0002_auto_20150109_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='BussZone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u540d\u79f0')),
                ('code', models.CharField(max_length=20, verbose_name='\u4ee3\u7801')),
            ],
            options={
                'verbose_name': '\u5546\u5708',
                'verbose_name_plural': '\u5546\u5708',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u540d\u79f0')),
                ('code', models.CharField(max_length=20, verbose_name='\u4ee3\u7801')),
                ('buildyear', models.IntegerField(verbose_name='\u5efa\u6210\u5e74\u5e95')),
                ('busszone', models.ForeignKey(to='webcrawler.BussZone')),
            ],
            options={
                'verbose_name': '\u5c0f\u533a',
                'verbose_name_plural': '\u5c0f\u533a',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Crawlerdb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=50, verbose_name='\u6293\u53d6\u7c7b\u522b')),
                ('starttime', models.DateTimeField(verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('endtime', models.DateTimeField(verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('newdatanum', models.IntegerField(verbose_name='\u65b0\u6570\u636e\u6570\u91cf')),
                ('olddatanum', models.IntegerField(verbose_name='\u91cd\u590d\u6570\u636e\u6570\u91cf')),
            ],
            options={
                'verbose_name': '\u6293\u53d6\u8bb0\u5f55',
                'verbose_name_plural': '\u6293\u53d6\u8bb0\u5f55',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u540d\u79f0')),
                ('code', models.CharField(max_length=20, verbose_name='\u4ee3\u7801')),
            ],
            options={
                'verbose_name': '\u533a\u57df',
                'verbose_name_plural': '\u533a\u57df',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('code', models.CharField(max_length=30, verbose_name='\u7f16\u53f7')),
                ('bedroom', models.IntegerField(verbose_name='\u5367\u5ba4')),
                ('liveroom', models.IntegerField(verbose_name='\u5ba2\u5385')),
                ('orien', models.CharField(max_length=20, verbose_name='\u671d\u5411')),
                ('floors', models.CharField(max_length=20, verbose_name='\u697c\u5c42')),
                ('allfloors', models.IntegerField(verbose_name='\u697c\u5c42\u603b\u6570')),
                ('area', models.IntegerField(verbose_name='\u9762\u79ef')),
                ('community', models.ForeignKey(to='webcrawler.Community')),
            ],
            options={
                'verbose_name': '\u623f\u5c4b',
                'verbose_name_plural': '\u623f\u5c4b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HousePrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.IntegerField(verbose_name='\u4ef7\u683c')),
                ('datetime', models.DateTimeField(verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('house', models.ForeignKey(to='webcrawler.House')),
            ],
            options={
                'verbose_name': '\u4ef7\u683c',
                'verbose_name_plural': '\u4ef7\u683c',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='busszone',
            name='district',
            field=models.ForeignKey(to='webcrawler.District'),
            preserve_default=True,
        ),
    ]
