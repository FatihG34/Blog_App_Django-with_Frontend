from rest_framework import viewsets
from rest_framework import generics
from blogApp.models import (
    BlogPost,
    Category,
    Comment,
    Like,
    View,

)
from .serializers import (
    CategorySerializer,
    BlogPostSerializer,
    LikeSerializer,
    CommentSerialzer,
    ViewSerializer
)


# class CategoryView(viewsets.ModelViewSet):
class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BlogPostUDView(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "slug"

# class BlogPostView(viewsets.ModelViewSet):
class BlogPostView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class LikeView(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerialzer


class ViewView(viewsets.ModelViewSet):
    queryset = View.objects.all()
    serializer_class = ViewSerializer
