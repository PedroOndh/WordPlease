from django.db import models

# Create your models here.

class Blog(models.Model):

    LIGHT = 'light'

    DARK = 'dark'

    STYLES = [
        [LIGHT, 'Light version'],
        [DARK, 'Dark version']
    ]

    name = models.CharField(max_length=150)

    description = models.TextField(null=True, blank=True, max_length=400)

    creation_date = models.DateTimeField(auto_now_add=True)

    modification_date = models.DateTimeField(auto_now=True)

    style = models.CharField(max_length=5, choices=STYLES)

    def __str__(self):
        return self.name


class Post(models.Model):

    # blog = models.ForeignKey(Blog, related_name="posts", on_delete=models.CASCADE)  # Allows access to posts from Blogs.posts instead of Blogs.post_set

    title = models.CharField(max_length=250)

    content = models.TextField()

    image_url = models.URLField(blank=True, null=True)

    creation_date = models.DateTimeField(auto_now_add=True)

    modification_date = models.DateTimeField(auto_now=True)

    # categories = models.ManyToManyField(Category, related_name="posts")  # Allows access to posts from Category.posts instead of Blogs.category_set

    def __str__(self):
        return self.title