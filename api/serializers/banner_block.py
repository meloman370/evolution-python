from rest_framework import serializers
from api.models import BannerBlock

class BannerBlockCreateSerializer(serializers.ModelSerializer):
  type = serializers.HiddenField(default="banner")
  class Meta:
    model = BannerBlock
    exclude = ['compressed_image']

class BannerBlockSerializer(serializers.ModelSerializer):
  class Meta:
    model = BannerBlock
    fields = '__all__'