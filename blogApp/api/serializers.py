from dataclasses import fields
from rest_framework import serializers

from blogApp.models import BlogPost, Category, Comment, Like, View


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name"
        )


class BlogPostSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField()
    # category_id = serializers.IntegerField()
    like_count = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    post_view_count = serializers.SerializerMethodField()
    class Meta:
        model = BlogPost
        fields = (
            "id",
            "title",
            "author",
            "category",
            # "category_id",
            "content",
            "image",
            "published_date",
            "updated_date",
            "status",
            "slug",
            "like_count",
            "comment_count",
            "post_view_count",
        )
        read_only_fields = (
            "published_date",
            "updated_date",
            "slug" 
        )

    def get_like_count(self, obj):
        return Like.objects.filter(post=obj.id).count()

    def get_comment_count(self, obj):
        return Comment.objects.filter(blog=obj.id).count()

    def get_post_view_count(self, obj):
        return View.objects.filter(post=obj.id).count()


class CommentSerialzer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()
    blog = serializers.StringRelatedField()
    blog_id = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = (
            "id",
            "content",
            "time_stamp",
            "user",
            "user_id",
            "blog",
            "blog_id"
        )


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            "id",
            "user",
            "post"
        )


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = (
            "id",
            "post",
            "user",
            "view_time"
        )
