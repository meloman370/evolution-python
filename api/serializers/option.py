from rest_framework import serializers
from api.models import Option, ProductOptions, OptionGroup

class ProductOptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductOptions
    fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = OptionGroup
    fields = ['id', 'name', 'machine_name']

class OptionSerializer(serializers.ModelSerializer):
  group = GroupSerializer()
  class Meta:
    model = Option
    exclude = ['products']