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


# class CategoryView(generics.ListCreateAPIView):
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class BlogPostView(generics.ListCreateAPIView):
class BlogPostView(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "slug"


class LikeView(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        
        return super().create(request, *args, **kwargs)


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerialzer


class ViewView(viewsets.ModelViewSet):
    queryset = View.objects.all()
    serializer_class = ViewSerializer
