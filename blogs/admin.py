from django.contrib import admin

# Register your models here.
from blogs.models import Post

admin.site.register(Post)