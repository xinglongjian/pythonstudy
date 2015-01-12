#!/usr/bin/env python
# coding=utf-8
from webcrawler.models import Province,City,Weather
import httplib2
import json
from decimal import *

def weatherAPIInvoke():
    h=httplib2.Http()
    city_list=City.objects.all()
    for city in city_list:
        if city.cityCode!="":
            saveWeather(h,city)
        else:
            cityapi="http://apistore.baidu.com/microservice/cityinfo"
            cityapi=cityapi+"?cityname="+city.cityName
            (resp, content) = h.request(cityapi, "GET")
            print content
            jsonresult=json.loads(content)
            if jsonresult['errNum']==0:
               cityname=jsonresult['retData']['cityName']
               c=City.objects.get(cityName=cityname)
               c.cityCode=jsonresult['retData']['cityCode']
               c.zipCode=jsonresult['retData']['zipCode']
               c.telAreaCode=jsonresult['retData']['telAreaCode']
               c.save()
               saveWeather(h,c)
            cityapi="";
        

def saveWeather(h,city):
    weatherapi="http://apistore.baidu.com/microservice/weather?cityid="+city.cityCode
    (resp, content) = h.request(weatherapi, "GET")
    weatherjson=json.loads(content)
    if weatherjson['errNum']==0:
        cityname=weatherjson['retData']['city']
        city_id=weatherjson['retData']['citycode']
        date="20"+weatherjson['retData']['date']
        time=weatherjson['retData']['time']
        try:
            w=Weather.objects.get(city=city,date=date,time=time)
            return;
        except Weather.DoesNotExist:
            temp=int(weatherjson['retData']['temp'])
            ltmp=weatherjson['retData']['l_tmp']
            l_tmp=int(ltmp[:len(ltmp)-1])
            htmp=weatherjson['retData']['h_tmp']
            h_tmp=int(htmp[:len(htmp)-1])
            w=Weather(city=city,date=date,time=time,weather=weatherjson['retData']['weather'],temp=temp,l_tmp=l_tmp,h_tmp=h_tmp,
            WD=weatherjson['retData']['WD'],WS=weatherjson['retData']['WS'])
            w.save()
    weatherapi="";
