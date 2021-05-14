from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "author", "post", "created_at", "updated_at")
        model = Post
