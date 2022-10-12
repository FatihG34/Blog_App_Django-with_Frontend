from django.contrib import admin

from blogApp.models import BlogPost, Category, Comment, Like, View

# Register your models here.
admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(View)