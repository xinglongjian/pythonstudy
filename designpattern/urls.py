from django.conf.urls import patterns,url

from designpattern import views

urlpatterns=patterns('',
    # ex: /polls/
    url(r'^$',views.index,name='index'),
    #url(r'^overall/',views.overall,name='overall'),
    url(r'^abstractfactory/',views.abstractfactory,name='abstractfactory'),
    # ex: /polls/5/
    )