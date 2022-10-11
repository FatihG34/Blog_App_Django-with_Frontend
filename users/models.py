from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_pic = models.URLField(max_length=200)
    biography = models.TextField()
    