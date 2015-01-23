#!/usr/bin/env python
# coding=utf-8
import os
from lxml import html
import time
import urllib2
import re
from webcrawler.models import Crawlerdb,District,BussZone,Community,House,HousePrice
import sys
from datetime import datetime
import pytz

DATE_FMT = '%Y-%m-%d'
tz = pytz.timezone('Asia/Shanghai')

#抓取小区信息进行存储，如果已经抓取过就不用再抓取了
def HouseCommunity():
    path="static/hcomm.install"
    if os.path.exists(path):
        print 'file hcomm.install exist!'
        return;
    else:
        #delete all data also CASCADE 
        District.objects.all().delete()
        
        try:
            commurl="http://bj.5i5j.com/community/"
            str = urllib2.urlopen(commurl,timeout=100).read().decode("utf-8")
            ll = html.fromstring(str)
        
            nodes=ll.find_class("reorder")
            if len(nodes)==1:
               commnums=int(nodes[0].find("*font").text_content())
            pages=commnums/12
            print pages
            if pages*12 < commnums:
               pages=pages+1
               
            failedurls=[] # list for failed urls
            count=1
            for i in range(1,pages):
               count=1
               commurl="http://bj.5i5j.com/community/n%s/" % i
               try:
                   str = urllib2.urlopen(commurl,timeout=300).read().decode("utf-8")
                   parseCommunity(str)
                   commurl=""
                   print i*12
                   time.sleep(5)
               except urllib2.HTTPError,e:
                   while count<=3:
                       try:
                           time.sleep(5)
                           print "%s urlopen failed count =%s" % (commurl,count)
                           str = urllib2.urlopen(commurl,timeout=300).read().decode("utf-8")
                           parseCommunity(str)
                           commurl=""
                           return
                       except urllib2.HTTPError, e:
                           count=count+1
                       
                   print "add %s to failedurls list" % commurl
                   failedurls.append(commurl)
                   continue
               except Exception,e:
                   continue
            #check the failed urls   
            if len(failedurls)>0:
                for furl in failedurls:
                   try:
                      str = urllib2.urlopen(furl,timeout=300).read().decode("utf-8")
                      parseCommunity(str)
                      time.sleep(10)
                   except urllib2.HTTPError,e:
                      print e.code
                      continue
                   except Exception,e:
                      continue
            print "save all data"
            os.mknod("static/hcomm.install")
        except urllib2.HTTPError,e:
            print "HouseCommunity HTTPError"
            print e.code
            return
        
        

#解析抓取的内容，封装成对象进行存储                
def parseCommunity(content):
    ll = html.fromstring(content)
    divs=ll.find_class("house-list695")[0]
    lists=divs.findall("li")
    for d in lists:
        comm_a=d.find_class("xqbt")[0].find("a")
        comm_name=comm_a.text_content()
        comm_url=comm_a.get("href")
        if comm_url!=None :
            comm_code=comm_url.split("/")[2]
        
        p_a_nodes=d.find_class("add1015")[0].findall('a')
        if len(p_a_nodes)==2:
            dist_node=p_a_nodes[0]
            bz_node=p_a_nodes[1]
            
            #District
            dist_name=dist_node.text_content()
            dist_code=dist_node.get("href").split("/")[2]
            try:
                distdata=District.objects.get(code=dist_code)
            except District.DoesNotExist:
                distdata=District(name=dist_name.encode('utf-8'),code=dist_code.encode('utf-8'))
                distdata.save()
            #BussZone
            buss_name=bz_node.text_content()
            buss_code=bz_node.get("href").split("/")[2]
            try:
                bussdata=BussZone.objects.get(district=distdata,code=buss_code)
            except BussZone.DoesNotExist:
                bussdata=BussZone(name=buss_name.encode('utf-8'),code=buss_code.encode('utf-8'),district=distdata)
                bussdata.save()
            
        patt=re.compile(r"(\d+)")
        data1015=d.find_class("data1015")[0].text_content() 
        data1015s=patt.findall(data1015)
        if len(data1015s)>0:
           buildyear=int(data1015s[0])
        else:
           buildyear=0
        try:
            community=Community.objects.get(busszone=bussdata,code=comm_code)
        except Community.DoesNotExist:
            community=Community(busszone=bussdata,name=comm_name.encode('utf-8'),code=comm_code.encode('utf-8'),buildyear=buildyear)
            community.save()
        
#抓取房屋信息,房源的基本信息一般不变，主要是修改时间及价格            
def CrawlerHouse():
    
    try:
        commurl="http://bj.5i5j.com/exchange/"
        str = urllib2.urlopen(commurl,timeout=300).read().decode("utf-8")
        ll = html.fromstring(str)
        
        nodes=ll.find_class("reorder")
        if len(nodes)==1:
            commnums=int(nodes[0].find("*font").text_content())
        divs=ll.find_class("house-list695")[0]
        num=len(divs.findall("li"))
        pages=commnums/num
        if pages*num < commnums:
            pages=pages+1
        print pages
        count=1
        failedurls=[] # list for failed urls
        for i in range(1,pages):
            count=1
            commurl="http://bj.5i5j.com/exchange/n%s/" % i
            try:
                print commurl
                str = urllib2.urlopen(commurl,timeout=300).read().decode("utf-8")
                parseHouse(str)
                commurl=""
                #print i*12
                time.sleep(10)
            except urllib2.HTTPError,e:
                while count<=3:
                    try:
                        time.sleep(5)
                        print "%s urlopen failed count =%s" % (commurl,count)
                        str = urllib2.urlopen(commurl,timeout=300).read().decode("utf-8")
                        parseHouse(str)
                        commurl=""
                        if True:break
                    except urllib2.HTTPError, e:
                           count=count+1
                else:
                    failedurls.append(commurl)
                #print e.code
                continue
            except Exception,e:
                continue
        #check the failed urls   
        if len(failedurls)>0:
            for furl in failedurls:
                try:
                    str = urllib2.urlopen(furl,timeout=300).read().decode("utf-8")
                    parseHouse(str)
                    time.sleep(5)
                except urllib2.HTTPError,e:
                    print e.code
                    continue
                except Exception,e:
                    continue
        print "save all data"    
    except urllib2.HTTPError,e:
        print "HouseCommunity HTTPError"
        print e.code
        return
        
#解析房屋信息        
def parseHouse(content):        
    ll = html.fromstring(content)
    divs=ll.find_class("house-list695")[0]
    lists=divs.findall("li")
    for d in lists:
        ht_a=d.find_class("maintitle")[0].find("a")
        house_title=ht_a.text_content()
        house_url=ht_a.get("href")
        if house_url!=None :
            house_code=house_url.split("/")[2]
        
        patt=re.compile(r"(\d+)")
        h3=d.find_class("house-info-col")[0].find("h3")
        spans=h3.findall("span")
        if len(spans)==3:
            span_one=spans[0]
            orien=span_one.text_content().strip()
            
            span_two=spans[1].text_content()
            floor=span_two.split("/")[0]
            allfloors=patt.findall(span_two.split("/")[1])
            if len(allfloors)>0:
                allfloor=int(allfloors[0])
            else:
                allfloor=0
            
            span_three=spans[2].text_content()
            build_years=patt.findall(span_three)
            if len(build_years)>0:
                build_year=int(build_years[0])
            else:
                build_year=0
        
        comm_as=d.find_class("subtitle")[0].findall("*a")
        if len(comm_as)==3:
            comm_a=comm_as[0]
            comm_name=comm_a.text_content()
            comm_code=comm_a.get("href").split("/")[2]
            try:
                commobj=Community.objects.get(code=comm_code)
            except Community.DoesNotExist:
                busszone_a=comm_as[2]
                busszone_name=busszone_a.text_content()
                busszone_code=busszone_a.get("href").split("/")[2]
                try:
                    busszoneobj=BussZone.objects.get(code=busszone_code)
                    commobj=Community(busszone=busszoneobj,name=comm_name.encode('utf-8'),code=comm_code.encode('utf-8'),buildyear=build_year)
                    commobj.save()
                    print "community save.code=%s" % comm_code
                except BussZone.DoesNotExist:
                    dist_a=comm_as[1]
                    dist_code=dist_a.get("href").split("/")[2]
                    try:
                        distobj=District.objects.get(code=dist_code)
                        busszoneobj=BussZone(district=distobj,name=busszone_name.encode('utf-8'),code=busszone_code.encode('utf-8'))
                        busszoneobj.save()
                        commobj=Community(busszone=busszoneobj,name=comm_name.encode('utf-8'),code=comm_code.encode('utf-8'),buildyear=build_year)
                        commobj.save()
                        print "busszone save,name=%s.community save.name=%s" % (busszone_name,comm_name)
                    except Exception, e:
                        print "save busszone and community failed!busszone_code=%s,comm_code=%s" % (busszone_code,comm_code)
                        continue
        else:
            print 'subtitle -a len !=3'
                
        bs=d.find_class("subtitle")[0].findall("b")
        if len(bs)==3:
            b_second=bs[1]
            b_s_t=b_second.text_content()
            if len(b_s_t)==4:
                bedroom=int(b_s_t[0])
                liveroom=int(b_s_t[2])
            else:
                print "bedroom error : %s" % b_s_t
            
            b_three=bs[2].text_content()
            patt=re.compile(r"(\d+)")
            areas=patt.findall(b_three)
            if len(areas)>0:
                area=int(areas[0])
            else:
                area=0
        
        pattdate=re.compile(r"(\d{2}-\d{2} \d{2}:\d{2})")
        h4=d.find_class("house-info-col")[0].find("h4")
        pub_dates=pattdate.findall(h4.text_content())
        date=datetime.now(tz)
        if len(pub_dates)>0:
            publisdate=datetime.strptime("%s-%s:00" % (date.year,pub_dates[0]),'%Y-%m-%d %H:%M:%S')
        else:
            publisdate=date
        #print publisdate
        strong=d.find_class("house-price-col")[0].find("strong")
        price=int(strong.text_content())
        
        try:
            h=House.objects.get(code=house_code)
        except House.DoesNotExist:
            h=House(community=commobj,title=house_title.encode('utf-8'),code=house_code.encode('utf-8'),bedroom=bedroom,
            liveroom=liveroom,orien=orien.encode('utf-8'),floors=floor.encode('utf-8'),allfloors=allfloor,area=area)
            try:
                h.save()
            except Exception, e:
                print e
             
            print 'save house price first'
            hPrice=HousePrice(house=h,price=price,datetime=publisdate)
            hPrice.save()
        try:
            print 'save houde price,%s,%s,%s'% (h.code,price,publisdate)
            hPrice=HousePrice.objects.get(house=h,price=price,datetime=publisdate)
        except HousePrice.DoesNotExist:
            print 'save house second'
            hPrice=HousePrice(house=h,price=price,datetime=publisdate)
            hPrice.save()
        #print 'save over'
        