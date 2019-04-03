from rest_framework import serializers
from main_app.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('hash', 'title', 'author', 'upvotes', 'content')
