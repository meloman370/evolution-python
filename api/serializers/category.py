from rest_framework import serializers
from django.db.models import Max, Min
from api.models import Category, SubMenu, Menu
from api.serializers.option_group import OptionGroupSerializer
from api.serializers.product import ProductListSerializer

class CategorySerializer(serializers.ModelSerializer):
    groups = OptionGroupSerializer(many=True, allow_null=True, required=False)
    products = ProductListSerializer(many=True)
    class Meta:
        model = Category
        exclude = ['sub_menu_item']

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['compressed_image']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class SubMenuSerializer(serializers.ModelSerializer):
    menu_item = MenuSerializer()
    class Meta:
        model = SubMenu
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):
    max_price = serializers.SerializerMethodField()
    min_price = serializers.SerializerMethodField()
    sub_menu_item = SubMenuSerializer()
    class Meta:
        model = Category
        fields = '__all__'

    def get_max_price(self, category):
        return category.products.aggregate(Max('price'))['price__max']

    def get_min_price(self, category):
        return category.products.aggregate(Min('price'))['price__min']
