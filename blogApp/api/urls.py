from django.urls import path
from rest_framework import routers

from blogApp.api.views import CategoryView, LikeView, BlogPostView, CommentView, ViewView

# router = routers.DynamicRoute()
router = routers.DefaultRouter()
router.register('posts', BlogPostView)
router.register('category', CategoryView)
router.register('comment', CommentView)
router.register('view', ViewView)
router.register('like', LikeView)


urlpatterns = [

] 
urlpatterns += router.urls
