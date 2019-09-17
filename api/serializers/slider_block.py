from rest_framework import serializers
from api.models import SliderBlock, SliderProduct
from api.serializers.product import ProductListSerializer

class SliderBlockCreateSerializer(serializers.ModelSerializer):
  type = serializers.HiddenField(default="slider")
  class Meta:
    model = SliderBlock
    fields = '__all__'

class SliderBlockSerializer(serializers.ModelSerializer):
  products = ProductListSerializer(many=True)
  class Meta:
    model = SliderBlock
    fields = '__all__'


class SliderProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = SliderProduct
    fields = '__all__'