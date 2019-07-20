from rest_framework.serializers import ModelSerializer

from blogs.models import Post


class PostsListSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content_introduction', 'publishing_date']


class PostsSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'content_introduction', 'content_body', 'image_url', 'publishing_date', 'categories',
                  'creation_date', 'modification_date', 'owner']
        read_only_fields = ['id', 'creation_date', 'modification_date', 'owner']