from rest_framework import serializers
from api.models import Image

class ImageTeaserSerializer(serializers.ModelSerializer):
    origin = serializers.ImageField(source='origin_thumb')
    compressed = serializers.ImageField(source='compressed_thumb')
    class Meta:
        model = Image
        fields = ['id', 'origin', 'compressed', 'alt', 'color']

class ImageSerializer(serializers.ModelSerializer):
    origin = serializers.ImageField(source='origin_inner')
    compressed = serializers.ImageField(source='compressed_inner')
    class Meta:
        model = Image
        fields = ['id', 'origin', 'compressed', 'alt', 'color']

class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'alt', 'origin_inner', 'product', 'color']
