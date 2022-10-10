from tkinter.tix import Tree
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    STATUS = (
        ("d", "Draft"),
        ("p", "Published"),
    )
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name="post_category", on_delete=models.CASCADE)
    content = models.TextField()
    image = models.URLField(max_length=200)
    status = models.CharField(max_length=50, choices=STATUS)
    slug = models.SlugField()
    published_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

class Like(models.Model):
    post = models.ForeignKey(BlogPost, related_name="post_like", on_delete=models.CASCADE)
    user = models.CharField(max_length=50)

    def __str__(self):
        return self.user

class View(models.Model):
    post = models.ForeignKey(BlogPost, related_name="post_view", on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    view_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.user} viewed at {self.view_time}"

class Comment(models.Model):
    user = models.CharField(max_length=50)
    blog = models.ForeignKey(BlogPost, related_name="post_comment", on_delete=models.CASCADE)
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"added by {self.user} at {self.time_stamp}"
