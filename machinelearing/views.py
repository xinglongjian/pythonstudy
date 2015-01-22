#!/usr/bin/env python
# coding=utf-8
from django.shortcuts import render
from webcrawler.models import Community,House,HousePrice

import numpy as np
import pandas as pd

# Create your views here.
#-------------------Classification View-------------------------------------------
def classindex(request):
    return render(request,'machinelearing/classification/index.html',{"menu":"classification","submenu":"index"})
    
#-------------------Regression View-------------------------------------------    
def regreindex(request):
    return render(request,'machinelearing/regression/index.html',{"menu":"regression","submenu":"index"})

def singlevar(request):
    commids=Community.objects.filter(busszone_id=943).values_list("id")
    houseobjs=House.objects.filter(community_id__in=commids,bedroom=3,liveroom=1,orien=u'南北')
    houseobjs=houseobjs.values_list('id','area')
    datalist=[]
    for d in houseobjs:
        itemlist=[]
        itemlist.append(d[1])
        priceobjs=HousePrice.objects.filter(house_id=d[0])
        priceobj=priceobjs.order_by("-datetime")[0]
        itemlist.append(priceobj.price)
        datalist.append(itemlist)
    
    df=pd.DataFrame(datalist)
    
    print df
    
    return render(request,'machinelearing/regression/singlevar.html',{"menu":"regression","submenu":"singlevar"})

def multivar(request):
    return render(request,'machinelearing/regression/multivar.html',{"menu":"regression","submenu":"multivar"})

def polynomial(request):
    return render(request,'machinelearing/regression/polynomial.html',{"menu":"regression","submenu":"polynomial"})

#-------------------Clustering View-------------------------------------------    
def clusterindex(request):
    return render(request,'machinelearing/clustering/index.html',{"menu":"clustering","submenu":"index"})