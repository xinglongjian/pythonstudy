from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pythonstudy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$',views.home, name='home'),
    url(r'^$','home.views.index',name='home'),
    url(r'^about/','home.views.about',name='about'),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': 'static'}),
    url(r'^polls/',include('polls.urls',namespace='polls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^designpattern/', include('designpattern.urls',namespace='designpattern')),
    url(r'^visualization/', include('visualization.urls',namespace='visualization')),
    url(r'^dataanalysis/', include('dataanalysis.urls',namespace='dataanalysis')),
    url(r'^ml/', include('machinelearing.urls',namespace='ml')),
    url(r'^webcrawler/', include('webcrawler.urls',namespace='webcrawler')),
)
