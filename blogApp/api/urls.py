from django.urls import path
from blogApp.api.views import (
    CategoryView,
    LikeView,
    BlogPostView,
    BlogPostDetailView,
    CommentView,
    PostUserView,
    UserAllPosts
)


urlpatterns = [
    path("users/", PostUserView.as_view()),
    path("category/", CategoryView.as_view()),
    path("posts/", BlogPostView.as_view()),
    path("like/", LikeView.as_view()),
    path("all-posts/", UserAllPosts.as_view()),
    path("posts/<str:slug>/", BlogPostDetailView.as_view()),
    path("posts/<str:slug>/add_comment/", CommentView.as_view()),

]
