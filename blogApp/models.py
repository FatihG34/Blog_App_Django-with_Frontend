from email.policy import default
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


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
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, related_name="post_user", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="post_category", on_delete=models.CASCADE)
    content = models.TextField()
    image = models.URLField(max_length=200, blank=True,
                            default="https://gravatar.com/avatar/2074b7945e3c6c493b0b2b94b24c35c2?s=400&d=robohash&r=x")
    published_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS)
    slug = models.SlugField(blank=True, unique=True)


    def __str__(self):
        return self.title

class Like(models.Model):
    post = models.ForeignKey(BlogPost, related_name="post_like", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name="liked_user", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class View(models.Model):
    post = models.ForeignKey(BlogPost, related_name="post_view", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name="viewed_user", on_delete=models.CASCADE)
    view_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.user} viewed at {self.view_time}"

class Comment(models.Model):
    user = models.ForeignKey(
        User, related_name="comment_user", on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogPost, related_name="post_comment", on_delete=models.CASCADE)
    content = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"added by {self.user} at {self.time_stamp}"
