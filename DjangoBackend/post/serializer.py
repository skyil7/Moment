from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['pub_date', 'title', 'category', 'date', 'address', 'text', 'lat', 'lng', 'img']
        read_only_fields = ('pub_date',)