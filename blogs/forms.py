from django.forms import ModelForm

from blogs.models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content_introduction', 'content_body', 'image_url']
