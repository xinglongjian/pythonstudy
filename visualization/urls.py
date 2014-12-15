from django.conf.urls import patterns,url

from visualization import views

urlpatterns=patterns('',
    
     url(r'^$',views.index,name='index'),
     url(r'^books/',views.books,name='books'),
     url(r'^linechart/',views.linechart,name='linechart'),
     url(r'^histogram/',views.histogram,name='histogram'),
     url(r'^barchart/',views.barchart,name='barchart'),
    )
