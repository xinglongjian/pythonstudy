from django.conf.urls import patterns,url

from machinelearing import views

urlpatterns=patterns('',
    # ex: /polls/
    #===================Classification================================
    url(r'^classindex/',views.classindex,name='classindex'),
    
    
    #====================Regression===============================
    url(r'^regreindex/',views.regreindex,name='regreindex'),
    url(r'^singlevar/',views.singlevar,name='singlevar'),
    url(r'^multivar/',views.multivar,name='multivar'),
    url(r'^polynomial/',views.polynomial,name='polynomial'),
    
    #====================Clustering===============================
    url(r'^clusterindex/',views.clusterindex,name='clusterindex'),
    )