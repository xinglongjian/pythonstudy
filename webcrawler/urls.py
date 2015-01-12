from django.conf.urls import patterns,url

from webcrawler import views

urlpatterns=patterns('',
    
     url(r'^$',views.index,name='index'),
     #url(r'^gmail/$',views.gmail,name='gmail'),
     #url(r'^gsubmit/$',views.gsubmit,name='gsubmit'),
    )
