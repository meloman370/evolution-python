from django.shortcuts import render
from rest_framework import generics
from api.serializers.menu import MenuSerializer, MenuCreateSerializer
from api.models import Menu

class MenuCreateView(generics.CreateAPIView):
  serializer_class = MenuCreateSerializer

class MenuView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = MenuSerializer
  queryset = Menu.objects.all()

class MenuListView(generics.ListAPIView):
  serializer_class = MenuSerializer
  queryset = Menu.objects.all()