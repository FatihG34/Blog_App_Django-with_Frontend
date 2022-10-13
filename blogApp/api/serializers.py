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


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    # blog = serializers.StringRelatedField()
    # blog_id = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = (
            "id",
            "content",
            "time_stamp",
            "user",
            "user_id",
        )
        # read_only_fields =(
        #     "user",
        #     "user_id"
        # )


class BlogPostSerializer(serializers.ModelSerializer):
    post_comment = CommentSerializer(many=True, read_only=True)
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
            "post_comment"
        )
        read_only_fields = (
            "published_date",
            "updated_date",
            "slug",
        )

    def get_like_count(self, obj):
        return Like.objects.filter(post=obj.id).count()

    def get_comment_count(self, obj):
        return Comment.objects.filter(blog=obj.id).count()

    def get_post_view_count(self, obj):
        return View.objects.filter(post=obj.id).count()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            "id",
            "user",
            "post"
        )

    # def create(self, validated_data):
    #     print(self.context['request'].user)
    #     if validated_data['user'] == self.context['request'].user:
    #         print(validated_data)
    #         return super().create(validated_data)


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = (
            "id",
            "post",
            "user",
            "view_time"
        )
