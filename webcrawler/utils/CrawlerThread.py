#!/usr/bin/env python
# coding=utf-8
import threading
import time
from webcrawler.utils import WeatherCrawler,HouseCrawler

#用于抓取天气数据的线程
class WeatherThread(threading.Thread):
    
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id=id
    def run(self):
        while(True):
            WeatherCrawler.weatherAPIInvoke()
            time.sleep(1200)
            
#用于抓取房屋数据的线程
class HouseThread(threading.Thread):
    
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id=id
    def run(self):
        while(True):
            HouseCrawler.HouseCommunity()
            HouseCrawler.CrawlerHouse()
            time.sleep(1200)
            