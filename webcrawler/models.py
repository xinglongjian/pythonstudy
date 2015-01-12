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
        
    def __str__(self):
        return u'%s %s %s' % (self.city.cityName,self.date,self.time)