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
from webcrawler.models import Province,City,Weather

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
