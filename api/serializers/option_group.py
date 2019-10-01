from rest_framework import serializers
from api.models import OptionGroup, CategoryOptionGroup
from api.serializers.option import OptionSerializer

class OptionGroupSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    class Meta:
        model = OptionGroup
        exclude = ['categories']

class OptionGroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionGroup
        fields = '__all__'

class CategoryOptionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryOptionGroup
        fields = '__all__'
