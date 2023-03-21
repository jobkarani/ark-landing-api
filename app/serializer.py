from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'methodologyTitle','methodology', 'about', 'location', 'tag', 'youtube_Video', 'webLink']


class BlogsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='blog_category.name')
    category_slug = serializers.CharField(source='blog_category.slug')
    category_id = serializers.IntegerField(source='blog_category.id')
    class Meta:
        model = Blogs
        fields = ['id', 'image', 'heading', 'created_at', 'text','tex2','text3','category_name','category_slug', 'category_id']

class BlogCategorySerializer(serializers.ModelSerializer):
    blogs = BlogsSerializer(many=True, read_only=True)
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'slug', 'blogs']