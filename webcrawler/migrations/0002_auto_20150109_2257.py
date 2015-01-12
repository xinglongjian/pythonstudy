# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webcrawler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cityName', models.CharField(max_length=20, verbose_name='\u57ce\u5e02\u540d')),
                ('cityCode', models.CharField(max_length=20, verbose_name='\u57ce\u5e02\u7f16\u7801', blank=True)),
                ('zipCode', models.CharField(max_length=20, verbose_name='\u90ae\u653f\u7f16\u7801', blank=True)),
                ('telAreaCode', models.CharField(max_length=20, verbose_name='\u7535\u8bdd\u533a\u53f7', blank=True)),
            ],
            options={
                'verbose_name': '\u57ce\u5e02',
                'verbose_name_plural': '\u57ce\u5e02',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provinceName', models.CharField(max_length=20, verbose_name='\u7701\u540d')),
            ],
            options={
                'verbose_name': '\u7701\u4efd',
                'verbose_name_plural': '\u7701\u4efd',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='\u65e5\u671f')),
                ('time', models.TimeField(verbose_name='\u65f6\u95f4')),
                ('weather', models.CharField(max_length=50, verbose_name='\u5929\u6c14')),
                ('temp', models.IntegerField(verbose_name='\u5f53\u524d\u6e29\u5ea6')),
                ('l_tmp', models.IntegerField(verbose_name='\u6700\u4f4e\u6c14\u6e29')),
                ('h_tmp', models.IntegerField(verbose_name='\u6700\u9ad8\u6c14\u6e29')),
                ('WD', models.CharField(max_length=20, verbose_name='\u98ce\u5411')),
                ('WS', models.CharField(max_length=20, verbose_name='\u98ce\u901f')),
                ('city', models.ForeignKey(to='webcrawler.City')),
            ],
            options={
                'verbose_name': '\u5929\u6c14',
                'verbose_name_plural': '\u5929\u6c14',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(to='webcrawler.Province'),
            preserve_default=True,
        ),
    ]
