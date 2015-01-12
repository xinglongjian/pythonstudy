from django.contrib import admin
from blogs.models import Category
from blogs.models import Blog
from blogs.models import Comment
# Register your models here.

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment)