from .models import Blog, Tag

from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag

class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Blog
        fields = ('id','title','content','create_time','pinned','abstract','subtitle','tags')
