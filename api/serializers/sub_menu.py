from rest_framework import serializers
from api.models import SubMenu
from api.serializers.category import CategoryListSerializer

class SubMenuSerializer(serializers.ModelSerializer):
    ategory = CategoryListSerializer(many=True)
    class Meta:
        model = SubMenu
        exclude = ['menu_item']

class SubMenuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenu
        fields = '__all__'
