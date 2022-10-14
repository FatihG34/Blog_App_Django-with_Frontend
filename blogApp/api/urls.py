from django.urls import path
from blogApp.api.views import (
    CategoryView,
    LikeView,
    BlogPostView,
    BlogPostDetailView,
    CommentView
)
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('posts', BlogPostView)
# router.register('category', CategoryView)
# router.register('comment', CommentView)
# router.register('view', ViewView)
# router.register('like', LikeView)


urlpatterns = [
    path("category/", CategoryView.as_view()),
    path("posts/", BlogPostView.as_view()),
    path("like/", LikeView.as_view()),
    path("posts/<str:slug>/", BlogPostDetailView.as_view()),
    path("posts/<str:slug>/add_comment/", CommentView.as_view()),

]
# urlpatterns += router.urls
