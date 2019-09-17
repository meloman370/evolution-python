from rest_framework import serializers
from api.models import Option, ProductOptions

class ProductOptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductOptions
    fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Option
    exclude = ['products']