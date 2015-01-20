#!/usr/bin/env python
# coding=utf-8
import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pythonstudy.settings")

    from django.core.management import execute_from_command_line
    
    #AppRegistryNotReady
    import django
    django.setup()
    
    from webcrawler.utils.CrawlerThread import WeatherThread,HouseThread
    
    #天气抓取线程
    wt=WeatherThread(23)
    wt.setDaemon(True) 
    wt.start()
    
    #房屋抓取线程
    ht=HouseThread(24)
    ht.setDaemon(True) 
    ht.start()
    
    execute_from_command_line(sys.argv)
