import threading
import time
from webcrawler.utils import WeatherCrawler

class MyThread(threading.Thread):
    
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id=id
    def run(self):
        while(True):
            WeatherCrawler.weatherAPIInvoke()
            time.sleep(600)