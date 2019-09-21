from django.shortcuts import render
from rest_framework import generics
from api.serializers.product_category import ProductCategorySerializer
from api.models import ProductCategory

class ProductCategoryCreateView(generics.CreateAPIView):
  serializer_class = ProductCategorySerializer
