from rest_framework import serializers
from api.models import Product
from api.serializers.image import ImageTeaserSerializer, ImageSerializer
from api.serializers.option import OptionSerializer

class ProductListSerializer(serializers.ModelSerializer):
    images = ImageTeaserSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'discount', 'images']

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, allow_null=True, required=False)
    options = OptionSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'
