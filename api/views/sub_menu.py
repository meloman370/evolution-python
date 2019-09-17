from django.shortcuts import render
from rest_framework import generics
from api.serializers.sub_menu import SubMenuSerializer, SubMenuCreateSerializer
from api.models import SubMenu

class SubMenuCreateView(generics.CreateAPIView):
  serializer_class = SubMenuCreateSerializer

class SubMenuView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = SubMenuSerializer
  queryset = SubMenu.objects.all()

class SubMenuListView(generics.ListAPIView):
  serializer_class = SubMenuSerializer
  queryset = SubMenu.objects.all()