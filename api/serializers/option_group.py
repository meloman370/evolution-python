from rest_framework import serializers
from api.models import OptionGroup
from api.serializers.option import OptionSerializer

class OptionGroupSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    class Meta:
        model = OptionGroup
        fields = '__all__'

class OptionGroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionGroup
        fields = '__all__'
