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
    category = models.CharField(max_length=50)
    content = models.TextField()
    image = models.URLField(max_length=200)
    status = models.CharField(max_length=50, choices=STATUS)
    slug = models.SlugField()
    published_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title
