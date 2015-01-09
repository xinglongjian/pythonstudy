from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from collections import defaultdict,Counter
from pandas import DataFrame,Series
import matplotlib
matplotlib.use('Agg') #
import matplotlib.pyplot as plt
import json
import types
import logging
import numpy as np
import pandas as pd

# Create your views here.

def index(request):
    return render(request,'dataanalysis/index.html',{'menu':'study','submenu':'index'})

#-----------------------------------------------------------------  
def study(request):
    '''
    study
    '''
    return render(request,'dataanalysis/study.html',{'menu':'study','submenu':'study'})

def getIndexOne(request):
    path='static/data/usagov_bitly_data2012-03-16-1331923249.txt'
    records=[json.loads(line) for line in open(path)]
    return JsonResponse(records[0])
    
def gettimezone(request):
    path='static/data/usagov_bitly_data2012-03-16-1331923249.txt'
    records=[json.loads(line) for line in open(path)]
    time_zones=[rec['tz'].encode("ascii") for rec in records if 'tz' in rec]
    return HttpResponse(str(time_zones[:10]))
    
def getTimezoneNum(request):
    
    path='static/data/usagov_bitly_data2012-03-16-1331923249.txt'
    records=[json.loads(line) for line in open(path)]
    time_zones=[rec['tz'] for rec in records if 'tz' in rec]
    counts=Counter(time_zones)
    ordercounts=counts.most_common(10)
    return JsonResponse(ordercounts,safe=False)

def getTimezoneNumByPandas(request):
    path='static/data/usagov_bitly_data2012-03-16-1331923249.txt'
    records=[json.loads(line) for line in open(path)]
    frame = DataFrame(records)
    clean_tz=frame['tz'].fillna('Missing')
    clean_tz[clean_tz=='']='Unknown'
    tz_counts = clean_tz.value_counts().order(ascending=True)
    
    plt.figure(figsize=(8,6), dpi=80)
    tz_counts[-10:].plot(kind='bar',rot=45)
    plt.savefig('static/plot/study/time_zones.png')
    return JsonResponse(tz_counts[-10:].to_json(),safe=False)

def urlEchartData(request):
    path='static/data/usagov_bitly_data2012-03-16-1331923249.txt'
    records=[json.loads(line) for line in open(path)]
    frame = DataFrame(records)
    clean_tz=frame['tz'].fillna('Missing')
    clean_tz[clean_tz=='']='Unknown'
    tz_counts = clean_tz.value_counts().order(ascending=True)
    tz_keys=[tz.encode('ascii') for tz in tz_counts[-10:].keys().tolist()]
    tz_values=tz_counts[-10:].values.tolist()
    data={"key":tz_keys,"values":tz_values}
    return JsonResponse(data,safe=False)
    

def getTzWindowsByPandas(request):
    path='static/data/usagov_bitly_data2012-03-16-1331923249.txt'
    records=[json.loads(line) for line in open(path)]
    frame = DataFrame(records)
    cframe = frame[frame.a.notnull()]
    oper_system=np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
    by_tz_os=cframe.groupby(['tz',oper_system])
    agg_counts=by_tz_os.size().unstack().fillna(0)
    indexer=agg_counts.sum(1).argsort()
    count_subset=agg_counts.take(indexer)[-10:]
    
    plt.figure(figsize=(8,6), dpi=80)
    count_subset.plot(kind='barh',rot=45,stacked=True)
    plt.savefig('static/plot/study/tz_opersystem.png')
    return JsonResponse({"result":"true"})

def urlOpEchartData(request):
    path='static/data/usagov_bitly_data2012-03-16-1331923249.txt'
    records=[json.loads(line) for line in open(path)]
    frame = DataFrame(records)
    cframe = frame[frame.a.notnull()]
    oper_system=np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
    by_tz_os=cframe.groupby(['tz',oper_system])
    agg_counts=by_tz_os.size().unstack().fillna(0)
    indexer=agg_counts.sum(1).argsort()
    count_subset=agg_counts.take(indexer)[-10:]
    
    keys=[x.encode('ascii') for x in count_subset.keys().tolist()]
    indexs=[x.encode('ascii') for x in count_subset.index.tolist()]
    colum1=[x for x,y in count_subset.values]
    colum2=[y for x,y in count_subset.values]
    data={"keys":keys,"indexs":indexs,"colum1":colum1,"colum2":colum2}
    return JsonResponse(data,safe=False)

#get Count
def get_count(sequence):
    counts=defaultdict(int)
    for x in sequence:
        counts[x]+=1
    return counts
    
    
def top_count(count_dict,n=10):
    #dict has no sort() function,list has.    
    value_key_pairs=[(count,tz) for tz,count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
    
#---------------------movielens---------------------------------------------------------
def movielens(request):
    
    #unames=['user_id','gender','age','occupation','zip']
    #users=pd.read_table('static/data/ml-1m/users.dat',engine='python',sep='::',header=None,names=unames)
    
    #rnames=['user_id','movie_id','rating','timestamp']
    #ratings=pd.read_table('static/data/ml-1m/ratings.dat',engine='python',sep='::',header=None,names=rnames)
    
    #mnames=['movie_id','title','genres']
    #movies=pd.read_table('static/data/ml-1m/movies.dat',engine='python',sep='::',header=None,names=mnames)
    
    return render(request,'dataanalysis/movielens.html',{'menu':'study','submenu':'movielens'})

#-------------------babynames--------------------------------------------------------------
def babynames(request):
    
    return render(request,'dataanalysis/babynames.html',{'menu':'study','submenu':'babynames'})