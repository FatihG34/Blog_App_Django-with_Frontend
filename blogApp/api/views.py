from urllib import request
from rest_framework import viewsets, generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
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
    CommentSerializer,
    ViewSerializer
)
from django.contrib.auth import get_user_model
# User = settings.AUTH_USER_MODEL
User = get_user_model()


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BlogPostView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    # lookup_field = "slug"


class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "slug"


class CommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        slug = self.kwargs.get('slug')
        blog = get_object_or_404(BlogPost, slug=slug)
        user = self.request.user
        comments = Comment.objects.filter(blog=blog, user=user)
        if comments.exists():
            raise ValidationError(
                "You can not add another comment, for this Post !")
        serializer.save(blog=blog, user=user)


class LikeView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        user = request.data.get('user')
        post = request.data.get('post')
        serializer = self.get_serializer(data=request.data)
        exists_like = Like.objects.filter(user=user, post=post)
        serializer.is_valid(raise_exception=True)
        if exists_like:
            exists_like.delete()
        else:
            self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ViewView(viewsets.ModelViewSet):
    queryset = View.objects.all()
    serializer_class = ViewSerializer
