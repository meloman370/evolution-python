from django.shortcuts import render
from rest_framework import generics
from api.serializers.sub_menu import SubMenuSerializer, SubMenuCreateSerializer
from api.models import SubMenu

class SubMenuCreateView(generics.CreateAPIView):
  serializer_class = SubMenuCreateSerializer

class SubMenuUpdateView(generics.UpdateAPIView):
  serializer_class = SubMenuCreateSerializer
  queryset = SubMenu.objects.all()

class SubMenuView(generics.RetrieveDestroyAPIView):
  serializer_class = SubMenuSerializer
  queryset = SubMenu.objects.all()

class SubMenuListView(generics.ListAPIView):
  serializer_class = SubMenuSerializer
  queryset = SubMenu.objects.all()