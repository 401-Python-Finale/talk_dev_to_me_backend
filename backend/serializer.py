from rest_framework import serializers
from .models import User_Profile

class User_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at')
        model = User_Profile