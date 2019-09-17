from rest_framework import serializers
from api.serializers.sub_menu import SubMenuSerializer
from api.models import Menu

class MenuSerializer(serializers.ModelSerializer):
  sub_menu = SubMenuSerializer(many=True)
  class Meta:
    model = Menu
    fields = '__all__'

class MenuCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Menu
    fields = '__all__'