#!/usr/bin/env python
# coding=utf-8
from django.shortcuts import render
from webcrawler.models import Community,House,HousePrice
from django.http import JsonResponse,HttpResponse
from webcrawler.models import Province,City,Weather,District,BussZone,Community,House,HousePrice
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create your views here.
#-------------------Classification View-------------------------------------------
def classindex(request):
    return render(request,'machinelearing/classification/index.html',{"menu":"machinelearing","dropmenu":"classification","submenu":"index"})
    
#-------------------Regression View-------------------------------------------    
def regreindex(request):
    return render(request,'machinelearing/regression/index.html',{"menu":"machinelearing","dropmenu":"regression","submenu":"index"})

def singlevar(request):
    districts=District.objects.all()
    return render(request,'machinelearing/regression/singlevar.html',{"menu":"machinelearing","dropmenu":"regression","submenu":"singlevar","districts":districts})

def singlehouse(request):
    bzid=request.GET.get("bzid")
    commid=request.GET.get("commid")
    room=request.GET.get("room")
    orien=request.GET.get("orien")
    area=request.GET.get("area")
    
    houseobjs=None;
    if commid!=None and commid!='null':
        houseobjs=House.objects.filter(community_id=commid,bedroom=room,orien=orien)
    else:
        commids=Community.objects.filter(busszone_id=bzid).values_list("id")
        houseobjs=House.objects.filter(community_id__in=commids,bedroom=room,orien=orien)
    
    if area!=None and area !='null':
        areas=area.split(",")
        houseobjs=houseobjs.filter(area__range=(int(areas[0]),int(areas[1])))
    
    houseobjs=houseobjs.values_list('id','area')
    if len(houseobjs)>0:
        datalist=[]
        for d in houseobjs:
           itemlist=[]
           itemlist.append(d[1])
           priceobjs=HousePrice.objects.filter(house_id=d[0])
           priceobj=priceobjs.order_by("-datetime")[0]
           itemlist.append(priceobj.price)
           datalist.append(itemlist)
        df=pd.DataFrame(datalist,columns=['area','price'])
    
        df=df.groupby('area').mean()
        df['area']=df.index
        X=[[x] for x in df.area.values]
        Y=[[y] for y in df.price.values]
    
        plt.figure(figsize=(7,5))
        plt.title('Price of House Against Area')
        plt.xlabel('Area(square meter)')
        plt.ylabel('Price(ten thousand)')
        plt.plot(X,Y,'r.')
        plt.grid(True)
        model=LinearRegression()
        model.fit(X,Y)
        X_Test=[[45],[85],[125],[160]]
        plt.plot(X_Test, model.predict(X_Test), 'b-',linewidth=1)
        plt.savefig('static/plot/house/singlehouse.png')
        data={"flag":"true"}
    else:
        data={"flag":"nodata"}
    return JsonResponse(data,safe=False)


def multivar(request):
    return render(request,'machinelearing/regression/multivar.html',{"menu":"machinelearing","dropmenu":"regression","submenu":"multivar"})

def polynomial(request):
    return render(request,'machinelearing/regression/polynomial.html',{"menu":"machinelearing","dropmenu":"regression","submenu":"polynomial"})

#-------------------Clustering View-------------------------------------------    
def clusterindex(request):
    return render(request,'machinelearing/clustering/index.html',{"menu":"machinelearing","dropmenu":"clustering","submenu":"index"})