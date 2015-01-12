#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pythonstudy.settings")

    from django.core.management import execute_from_command_line
    
    #AppRegistryNotReady
    import django
    django.setup()
    
    from webcrawler.utils.WeatherThread import MyThread
    t1=MyThread(23)
    t1.setDaemon(True) 
    t1.start()
    
    execute_from_command_line(sys.argv)
