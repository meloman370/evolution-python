from django.shortcuts import render
from rest_framework import generics
from api.serializers.option import OptionSerializer, ProductOptionSerializer
from api.models import Option, ProductOptions

class OptionCreateView(generics.CreateAPIView):
  serializer_class = OptionSerializer

class OptionView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = OptionSerializer
  queryset = Option.objects.all()

class OptionListView(generics.ListAPIView):
  serializer_class = OptionSerializer
  queryset = Option.objects.all()

class ProductOptionsCreateView(generics.CreateAPIView):
  serializer_class = ProductOptionSerializer