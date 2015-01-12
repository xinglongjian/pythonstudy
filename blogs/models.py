# coding=utf-8
from django.db import models
# Create your models here.

class Category(models.Model):
    name=models.CharField(u'分类名称',max_length=50)
    class Meta:
        verbose_name='分类'
        verbose_name_plural='分类中心'
    def __unicode__(self):
        return self.name
    
class Blog(models.Model):
    category=models.ForeignKey(Category)
    title=models.CharField(u'标题',max_length=150)
    blogboby=models.TextField(u'正文')
    timestamp = models.DateTimeField(u'时间')
    upnum=models.IntegerField(u'好评')
    downnum=models.IntegerField(u'差评')
    class Meta:
        verbose_name='文章'
        verbose_name_plural='博客'
    
    def __unicode__(self):
        return self.title
    
class Comment(models.Model):
    blog=models.ForeignKey(Blog)
    parentid=models.ForeignKey('self')
    content=models.TextField(u'评论')
    timestamp=models.DateTimeField(u'评论时间')
    address=models.CharField(u'IP',max_length=30)
    
    class Meta:
        verbose_name='评论'
        verbose_name_plural='评论'
    
    def __unicode__(self):
        return self.content
    
