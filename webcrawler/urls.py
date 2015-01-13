from django.conf.urls import patterns,url

from webcrawler import views

urlpatterns=patterns('',
     url(r'^$',views.index,name='index'),
     url(r'^currTemp/',views.currTemp,name='currTemp'),
     url(r'^weekTemp/',views.weekTemp,name='weekTemp'),
     url(r'^clusterTemp/',views.clusterTemp,name='clusterTemp'),
    )
