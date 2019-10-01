from rest_framework import serializers
from api.models import Block
from api.serializers.slider_block import SliderBlockSerializer
from api.serializers.banner_block import BannerBlockSerializer

class BlockCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'

class BlockSerializer(serializers.ModelSerializer):
    slider = SliderBlockSerializer(many=True)
    banner = BannerBlockSerializer(many=True)

    class Meta:
        model = Block
        fields = '__all__'
