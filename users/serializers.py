from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class UserListSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username']


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'date_joined', 'last_login', 'password']
        read_only_fields = ['id', 'date_joined', 'last_login']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.set_password(validated_data.get('password'))
        instance.email = validated_data.get('email')
        instance.save()
        return instance


class BlogListSerializer(serializers.ModelSerializer):

    blog_url = serializers.SerializerMethodField()

    def get_blog_url(self, obj):
        return self.context.get('request').get_host() + '/' + str(obj.username)

    class Meta:
            model = User
            fields = ('username', 'blog_url')
