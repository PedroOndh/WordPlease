import datetime

from django.forms import ModelForm

from blogs.models import Post
from django import forms


class PostForm(ModelForm):

    publishing_date = forms.DateTimeField(initial=datetime.datetime.now())

    class Meta:
        model = Post
        fields = ['title', 'content_introduction', 'content_body', 'image_url', 'publishing_date', 'categories']
