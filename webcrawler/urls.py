from django.conf.urls import patterns,url

from webcrawler import views

urlpatterns=patterns('',
     url(r'^$',views.index,name='index'),
     url(r'^currTemp/',views.currTemp,name='currTemp'),
     url(r'^weekTemp/',views.weekTemp,name='weekTemp'),
     url(r'^clusterTemp/',views.clusterTemp,name='clusterTemp'),
     url(r'^house/',views.house,name='house'),
     url(r'^weather/',views.weather,name='weather'),
     url(r'^getWeatherJosn/',views.getWeatherJosn,name='getWeatherJosn'),
     url(r'^getHouseJosn/',views.getHouseJosn,name='getHouseJosn'),
     url(r'^getBussZoneJson/',views.getBussZoneJson,name='getBussZoneJson'),
     url(r'^getCommunityJson/',views.getCommunityJson,name='getCommunityJson'),
     url(r'^getSingleHouseJson/',views.getSingleHouseJson,name='getSingleHouseJson'),
     
    )
