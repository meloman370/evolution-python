from django.shortcuts import render
from rest_framework import generics
from api.serializers.product import ProductSerializer, ProductListSerializer, ProductCreateSerializer
from api.models import Product

class ProductCreateView(generics.CreateAPIView):
  serializer_class = ProductCreateSerializer

  

class ProductView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()

class ProductListView(generics.ListAPIView):
  serializer_class = ProductListSerializer
  queryset = Product.objects.all()

  def get_queryset(self):
    queryset = Product.objects.all()
    price_from = self.request.query_params.get('price_from', None)
    price_to = self.request.query_params.get('price_to', None)
    if price_from is not None:
      queryset = queryset.filter(price__gt=price_from)
    if price_to is not None:
      queryset = queryset.filter(price__lt=price_to)
    return queryset
