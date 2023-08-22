from rest_framework import serializers
from .models import BlogPost, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = '__all__'

class UpdateBlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'updated_at')
        read_only_fields = ('author', 'created_at')