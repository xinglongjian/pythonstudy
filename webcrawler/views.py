from django.shortcuts import render
import urllib2,cookielib
import urllib
import logging
#from webcrawler.models import GmailForm
##from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import RequestContext
from webcrawler.models import Province,City,Weather
# Create your views here.

def index(request):
    return render(request,'webcrawler/index.html',{"menu":"webcrawler","submenu":"index"})
#----------------------------------------------------------------------------------

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
