from rest_framework import serializers
from api.models import Category
from api.serializers.option_group import OptionGroupSerializer

class CategorySerializer(serializers.ModelSerializer):
  groups = OptionGroupSerializer(many=True, allow_null=True, required=False)
  class Meta:
    model = Category
    exclude = ['sub_menu_item']

class CategoryCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    exclude = ['compressed_image']

class CategoryListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'name', 'url_alias', 'image', 'compressed_image']