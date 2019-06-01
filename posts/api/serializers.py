from django.contrib.auth.models import User
from rest_framework import serializers
from posts.models import Post, Category


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", "slug"]


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'category']