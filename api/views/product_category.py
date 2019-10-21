from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
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

class ProductCategoryDeleteByProduct(APIView):
    def delete(self, request, pk):
        """
        Delete all by product
        """
        product_category = ProductCategory.objects.filter(product=pk)
        product_category.delete()
        return Response(status=status.HTTP_200_OK)
