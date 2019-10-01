from rest_framework import generics
from api.serializers.product_category import ProductCategorySerializer
from api.models import ProductCategory

class ProductCategoryCreateView(generics.CreateAPIView):
    serializer_class = ProductCategorySerializer

class ProductCategoryView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()

class ProductCategoryListView(generics.ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
