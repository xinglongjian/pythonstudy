from django.conf.urls import patterns,url

from visualization import views

urlpatterns=patterns('',
    
     url(r'^$',views.index,name='index'),
     url(r'^books/',views.books,name='books'),
     url(r'^linechart/',views.linechart,name='linechart'),
     url(r'^histogram/',views.histogram,name='histogram'),
     url(r'^barchart/',views.barchart,name='barchart'),
     url(r'^piechart/',views.piechart,name='piechart'),
     url(r'^bubblechart/',views.bubblechart,name='bubblechart'),
     url(r'^radarchart/',views.radarchart,name='radarchart'),
     url(r'^candlestickchart/',views.candlestickchart,name='candlestickchart'),
     
     #d3
     url(r'^d3index/',views.d3index,name='d3index'),
     url(r'^api_core/',views.api_core,name='api_core'),
     url(r'^api_svg/',views.api_svg,name='api_svg'),
    )
