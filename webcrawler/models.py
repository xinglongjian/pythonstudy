#!/usr/bin/env python
# coding=utf-8
from django.db import models

# Create your models here.
class Province(models.Model):
    provinceName=models.CharField(u'省名',max_length=20)
    class Meta:
        verbose_name='省份'
        verbose_name_plural='省份'
    def __unicode__(self):
        return self.provinceName

class City(models.Model):
    province=models.ForeignKey(Province)
    cityName=models.CharField(u'城市名',max_length=20)
    cityCode=models.CharField(u'城市编码',max_length=20,blank=True)
    zipCode=models.CharField(u'邮政编码',max_length=20,blank=True)
    telAreaCode=models.CharField(u'电话区号',max_length=20,blank=True)
    
    class Meta:
        verbose_name='城市'
        verbose_name_plural='城市'
    def __unicode__(self):
        return u'%s ：%s' % (self.cityName, self.cityCode)
    
class Weather(models.Model):
    city=models.ForeignKey(City)
    date=models.DateField(u'日期')
    time=models.TimeField(u'时间')
    weather=models.CharField(u'天气',max_length=50)
    temp=models.IntegerField(u'当前温度')
    l_tmp=models.IntegerField(u'最低气温')
    h_tmp=models.IntegerField(u'最高气温')
    WD=models.CharField(u'风向',max_length=20)
    WS=models.CharField(u'风速',max_length=20)
    
    class Meta:
        verbose_name='天气'
        verbose_name_plural='天气'
    def __unicode__(self):
        return u'%s %s' % (self.date, self.time)
        
class Crawlerdb(models.Model):
    category=models.CharField(u'抓取类别',max_length=50)
    starttime=models.DateTimeField(u'开始时间')
    endtime=models.DateTimeField(u'结束时间')
    newdatanum=models.IntegerField(u'新数据数量')
    olddatanum=models.IntegerField(u'重复数据数量')
    
    class Meta:
        verbose_name='抓取记录'
        verbose_name_plural='抓取记录'
    
    def __unicode__(self):
        return u'%s %s' % (self.category, self.starttime)
    
class District(models.Model):
    name=models.CharField(u'名称',max_length=30)
    code=models.CharField(u'代码',max_length=20)
    
    class Meta:
        verbose_name='区域'
        verbose_name_plural='区域'
        
    def __unicode__(self):
        return '%s %s' % (self.name, self.code)
        
        
class BussZone(models.Model):
    district=models.ForeignKey(District)
    name=models.CharField(u'名称',max_length=30)
    code=models.CharField(u'代码',max_length=20)
   
    class Meta:
        verbose_name='商圈'
        verbose_name_plural='商圈'
        
    def __unicode__(self):
        return '%s %s %s' % (self.district.name,self.name,self.code)
    
class Community(models.Model):
    busszone=models.ForeignKey(BussZone)
    name=models.CharField(u'名称',max_length=30)
    code=models.CharField(u'代码',max_length=20)
    buildyear=models.IntegerField(U'建成年底')
    
    class Meta:
        verbose_name='小区'
        verbose_name_plural='小区'
        
    def __unicode__(self):
        return '%s %s %s' % (self.busszone.name,self.name, self.code)
        
class House(models.Model):
    community=models.ForeignKey(Community)
    title=models.CharField(u'标题',max_length=100)
    code=models.CharField(u'编号',max_length=30)
    bedroom=models.IntegerField(u'卧室')
    liveroom=models.IntegerField(u'客厅')
    orien=models.CharField(u'朝向',max_length=20)
    floors=models.CharField(u'楼层',max_length=20)
    allfloors=models.IntegerField(u'楼层总数')
    area=models.IntegerField(u'面积')
    
    class Meta:
        verbose_name='房屋'
        verbose_name_plural='房屋'
        
    def __unicode__(self):
        return self.title
    
    
class HousePrice(models.Model):
    house=models.ForeignKey(House)
    price=models.IntegerField(u'价格')
    datetime=models.DateTimeField(u'添加时间')
    
    class Meta:
        verbose_name='价格'
        verbose_name_plural='价格'
        
    def __unicode__(self):
        return self.price