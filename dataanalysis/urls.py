from django.conf.urls import patterns,url

from dataanalysis import views

urlpatterns=patterns('',
    
    url(r'^$',views.index,name='index'),
    url(r'^study/',views.study,name='study'),
    url(r'^getIndexOne/',views.getIndexOne,name='getIndexOne'),
    url(r'^gettimezone/',views.gettimezone,name='gettimezone'),
    url(r'^getTimezoneNum/',views.getTimezoneNum,name='getTimezoneNum'),
    url(r'^getTimezoneNumByPandas/',views.getTimezoneNumByPandas,name='getTimezoneNumByPandas'),
    url(r'^urlEchartData/',views.urlEchartData,name='urlEchartData'),
    url(r'^getTzWindowsByPandas/',views.getTzWindowsByPandas,name='getTzWindowsByPandas'),
    url(r'^urlOpEchartData/',views.urlOpEchartData,name='urlOpEchartData'),
    
    #------------------------------
    url(r'^movielens/',views.movielens,name='movielens'),
    
    
    #-----------------------------------
    url(r'^babynames/',views.babynames,name='babynames'),
    )