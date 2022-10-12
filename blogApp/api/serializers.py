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
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()

    class Meta:
        model = BlogPost
        fields = (
            "id",
            "author",
            "category_id",
            "category",
            "content",
            "image",
            "published_date",
            "updated_date",
            "status"
        )
        read_only_fields = (
            "published_date",
            "updated_date",
        )


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
