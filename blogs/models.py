from datetime import timezone

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Post(models.Model):

    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    title = models.CharField(max_length=250)

    content_introduction = models.TextField()

    content_body = models.TextField()

    image_url = models.URLField(blank=True, null=True)

    publishing_date = models.DateTimeField()

    creation_date = models.DateTimeField(auto_now_add=True)

    modification_date = models.DateTimeField(auto_now=True)

    categories = models.ManyToManyField(Category, related_name="posts")

    def __str__(self):
        return self.title