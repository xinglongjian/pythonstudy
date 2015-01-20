#!/usr/bin/env python
# coding=utf-8
from django.shortcuts import render
import urllib2,cookielib
import urllib
import logging
from datetime import *
import pytz

#from webcrawler.models import GmailForm
##from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.template import RequestContext
from webcrawler.models import Province,City,Weather,District,BussZone,Community,House,HousePrice

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
# Create your views here.

DATE_FMT = '%Y-%m-%d'
tz = pytz.timezone('Asia/Shanghai')
def index(request):
    return render(request,'webcrawler/index.html',{"menu":"webcrawler","submenu":"index"})
#----------------------------------------------------------------------------------
#
def currTemp(request):
    date=datetime.now(tz)
    date=date.date
    city_id=request.GET.get("id")
    city=City.objects.get(id=city_id)
    bjtemp=Weather.objects.filter(city=city,date=date)
    keys=[k.time for k in bjtemp]
    values=[v.temp for v in bjtemp]
    legend=[city.cityName]
    data={"keys":keys,"values":values,"legend":legend}
    return JsonResponse(data,safe=False)

def weekTemp(request):
    date=datetime.now(tz)
    date=date+timedelta(days=-6)
    city_id=request.GET.get("id")
    city=City.objects.get(id=city_id)
    datelist=Weather.objects.filter(city=city,date__gte= date.date ).values("date").distinct()#date >= date+atime
    dates=[]
    htemps=[]
    ltemps=[]
    for d in datelist:
        wlist=Weather.objects.filter(city=city,date=d['date'])
        if len(wlist)>0:
            dates.append(wlist[0].date)
            harray=[e.temp for e in wlist]
            htemps.append(max(harray))
            ltemps.append(min(harray))
    
    data={"keys":dates,"htemps":htemps,"ltemps":ltemps}
    return JsonResponse(data,safe=False)


def clusterTemp(request):
    date=datetime.now(tz)
    date=date.date
    citys=City.objects.all()
    citylist=[]
    htemps=[]
    ltemps=[]
    for c in citys:
        datelist=Weather.objects.filter(city=c,date=date)
        if len(datelist)>0:
           citylist.append(c.cityName)
           htemps.append(datelist[0].h_tmp)
           ltemps.append(datelist[0].l_tmp)
    X1=np.array(htemps)
    X2=np.array(ltemps)
    ltarray=np.array(zip(X1,X2)).reshape(len(X1), 2) 
    kmeans=KMeans(init='k-means++', n_clusters=2, n_init=10)
    kmeans.fit(ltarray)
    one=kmeans.labels_[0]
    onecount=kmeans.labels_.tolist().count(one)
    data={"keys":citylist,"htemps":ltarray[:onecount].tolist(),"ltemps":ltarray[onecount:].tolist()}
    return JsonResponse(data,safe=False)

#def gmail(request):
   # content=urllib2.urlopen("http://mail.google.com/mail/").read()
#    content="dd"
    #urllib.urlretrieve("http://mail.google.com/mail/","static/gmail.html")
#    return render(request,'webcrawler/gmail/index.html',{"menu":"webcrawler","submenu":"gmail","content":content})
    
#@csrf_exempt   
#def gsubmit(request):
#    logging.info("come into ")
#    inputEmail = request.POST['inputEmail']
    # inputPassword = request.POST['inputPassword']
    # postdata = urllib.urlencode({
    #           "Email":inputEmail,
    #           "Passwd":inputPassword,
    #           "GALX":"SFno6Jal4ac",
    #           "continue":"http://mail.google.com/mail/",
    #           "service":"mail",
    #           "rm":"false",
    #           "ltmpl":"default",
    #           "scc":"1",
    #           "_utf8":"&#9731;",
    #           "bgresponse":"js_disabled",
    #           "PersistentCookie":"yes"
    # })
    
    # req=urllib2.Request(
    #     url='https://accounts.google.com/ServiceLoginAuth',
    #     data=postdata
    # )
    # cookie_support= urllib2.HTTPCookieProcessor(cookielib.CookieJar())
    # opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    # urllib2.install_opener(opener)
    # result = urllib2.urlopen(req).read()
    # return render(request,'webcrawler/gmail/gmailmain.html',{"menu":"webcrawler","submenu":"gmail","content":result})
#---------------------------------------------------------------------------------

def weather(request):
    citys=City.objects.all()
    return  render(request,'webcrawler/weather/index.html',{"menu":"webcrawler","submenu":"weather","citys":citys})

def getWeatherJosn(request):
    idraw=request.GET.get("sEcho")
    displayStart=int(request.GET.get("iDisplayStart"))
    displayLength=int(request.GET.get("iDisplayLength"))
    iSortCol_0=request.GET.get("iSortCol_0")
    sSortDir_0=request.GET.get("sSortDir_0")
    cityid=request.GET.get("cityid")
    datestr=request.GET.get("date")
    
    count=Weather.objects.count()
    
    weathObjs=Weather.objects.order_by('-date','-time').all()
    if cityid !='null':
        weathObjs=weathObjs.filter(city_id=cityid)
    if datestr !='null' and datestr !='':
        weathObjs=weathObjs.filter(date=datestr)
    filtercount=weathObjs.count()
    displayEnd=displayStart+displayLength
    alldatas=weathObjs[displayStart:displayEnd]
    datalist=[]
    for d in alldatas:
        itemlist=[]
        itemlist.append(d.city.cityName)
        itemlist.append(d.date)
        itemlist.append(d.time)
        itemlist.append(d.weather)
        itemlist.append(d.temp)
        itemlist.append(d.l_tmp)
        itemlist.append(d.h_tmp)
        itemlist.append(d.WD)
        itemlist.append(d.WS)
        datalist.append(itemlist)
    data={"draw":idraw,"recordsTotal":count,"recordsFiltered":filtercount,"data":datalist}
    return JsonResponse(data,safe=False)


def house(request):
    districts=District.objects.all()
    return render(request,'webcrawler/house/index.html',{"menu":"webcrawler","submenu":"house","districts":districts})
    
def getHouseJosn(request):
    idraw=request.GET.get("sEcho")
    displayStart=int(request.GET.get("iDisplayStart"))
    displayLength=int(request.GET.get("iDisplayLength"))
    iSortCol_0=request.GET.get("iSortCol_0")
    sSortDir_0=request.GET.get("sSortDir_0")
    bzid=request.GET.get("bzid")
    room=request.GET.get("room")
    orien=request.GET.get("orien")
    area=request.GET.get("area")
    price=request.GET.get("price")
    
    count=House.objects.count()
    
    houseObjs=House.objects.all()
    if bzid!=None and bzid !='null':
        commids=Community.objects.filter(busszone_id=bzid).values_list('id')
        houseObjs=houseObjs.filter(community_id__in=commids)
    if room!=None and room !='null':
        houseObjs=houseObjs.filter(bedroom=int(room))
    if orien !=None and orien !='null':
        houseObjs=houseObjs.filter(orien=orien)
    if area !=None and area !='null':
        areas=area.split(",")
        houseObjs=houseObjs.filter(area__range=(int(areas[0]),int(areas[1])))
    if price !=None and price!='null':
        prices=price.split(",")
        priceHids=HousePrice.objects.filter(price__range=(int(prices[0]),int(prices[1]))).values_list('house_id').distinct()
        houseObjs=houseObjs.filter(id__in=priceHids)
    filtercount=houseObjs.count()
    displayEnd=displayStart+displayLength
    alldatas=houseObjs[displayStart:displayEnd]
    datalist=[]
    for d in alldatas:
        itemlist=[]
        itemlist.append(d.community.name)
        itemlist.append(d.code)
        itemlist.append(d.bedroom)
        itemlist.append(d.liveroom)
        itemlist.append(d.orien)
        itemlist.append(d.floors)
        itemlist.append(d.allfloors)
        itemlist.append(d.area)
        priceobjs=HousePrice.objects.filter(house_id=d.id)
        priceobj=priceobjs.order_by("-datetime")[0]
        itemlist.append(priceobjs.count())
        itemlist.append(priceobj.price)
        datalist.append(itemlist)
    data={"draw":idraw,"recordsTotal":count,"recordsFiltered":filtercount,"data":datalist}
    return JsonResponse(data,safe=False)


def getBussZoneJson(request):
    disId=request.GET.get("disId")
    busszoneobjs=BussZone.objects.filter(district_id=disId)
    datalist=[]
    for d in busszoneobjs:
        itemlist=[]
        itemlist.append(d.id)
        itemlist.append(d.name)
        datalist.append(itemlist)
    data={"data":datalist}
    return JsonResponse(data,safe=False)